import random
import numpy as np
import flappy_bird_gym
from collections import deque

# neural network
from keras.layers import Input, Dense
from keras.models import load_model, save_model, Sequential
from keras.optimizers import RMSprop #optimizer


# Neural Network for Agent
def NeuralNetwork(input_shape, output_shape):
    model = Sequential()
    model.add(Input(input_shape))
    model.add(Dense(512, input_shape=input_shape, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(256, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(64, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(output_shape, activation='linear', kernel_initializer='he_uniform'))
    model.compile(loss='mse', optimizer=RMSprop(learning_rate=0.0001, rho=0.95, epsilon=0.01), metrics=['accuracy'])
    model.summary()
    return model


# Brain Agent for Flappy Bird
class DeepQAgent:
    def __init__(self):
        # Environment Variables
        self.env = flappy_bird_gym.make("FlappyBird-v0")
        self.episodes = 100
        self.state_space = self.env.observation_space.shape[0]
        self.action_space = self.env.action_space.n 
        # first agent act like database that this model will train from
        self.memory = deque(maxlen=2000)

        # Hyperparameters
        self.gamma = 0.96
        self.epsilon = 1
        self.epsilon_decay = 0.999 # untuk mengurangi nilai epsilon secara bertahap selama training agar agen dapat belajar secara efisien
        self.epsilon_min = 0.01 # agar agent dapat diatur untuk melakukan eksplorasi agar tidak terlalu percaya diri dan terjebak dalam lokal minimum.
        self.batch_number = 64 # sample training per episodes
        
        self.train_start = 1000 # minimum sample yang dibutuhkan agent sebelum masuk ke proses training
        self.jump_prob = 0.01
        self.model = NeuralNetwork(input_shape=(self.state_space,), output_shape=self.action_space)

    def action(self, state):
        if np.random.random() > self.epsilon:
            return np.argmax(self.model.predict(state))
        return 1 if np.random.random() < self.jump_prob else 0
    
    def learn(self):
        # Just make sure, we have enough data
        if len(self.memory) < self.train_start:
            return
        
        # Create minibatch
        minibatch = random.sample(self.memory, min(len(self.memory), self.batch_number))
        # Variables to store minibatch info
        state = np.zeros((self.batch_number, self.state_space))
        next_state = np.zeros((self.batch_number, self.state_space))

        action, reward, done = [], [], []

        # Store data in variables
        for i in range(self.batch_number):
            state[i] = minibatch[i][0]
            action.append(minibatch[i][1])
            reward.append(minibatch[i][2])
            next_state[i] = minibatch[i][3]
            done.append(minibatch[i][4])

        # Predict y label
        target = self.model.predict(state)
        target_next = self.model.predict(next_state)

        for i in range(self.batch_number):
            if done[i]:
                target[i][action[i]] = reward[i]
            else:
                target[i][action[i]] = reward[i] + self.gamma + (np.max(target_next[i]))

        print('train')
        self.model.fit(state, target, batch_size = self.batch_number, verbose=0)

    def train(self):
        # n Episode Iterations for training
        for i in range(self.episodes):
            # Env variables for training
            state = self.env.reset()
            state = np.reshape(state, [1, self.state_space])
            done = False
            score = 0
            self.epsilon = self.epsilon * self.epsilon_decay if self.epsilon * self.epsilon_decay > self.epsilon_min else self.epsilon_min

            while not done:
                self.env.render()
                action = self.action(state)
                next_state, reward, done, info = self.env.step(action)

                # reshape next state
                next_state = np.reshape(next_state, [1, self.state_space])
                score += 1

                if done:
                    # done means die
                    reward -= 100

                self.memory.append((state, action, reward, next_state, done))
                state = next_state

                if done:
                    print('Episode: {}\nScore: {}\nEpsilon: {:.2}'.format(i, score, self.epsilon))
                    # Save model
                    if score >= 130:
                        self.model.save('flappymodel.h5')
                        print("Model berhasil")
                        return 

                self.learn()

    # Visualize Model
    def perform(self):
        self.model = load_model('flappymodel.h5')
        highest_score = 0
        for i in range(2):
            state = self.env.reset()
            state = np.reshape(state, [1, self.state_space])
            done = False
            score = 0

            while not done:
                self.env.render()
                action = np.argmax(self.model.predict(state))
                next_state, reward, done, info = self.env.step(action)
                state = np.reshape(next_state, [1, self.state_space])
                score += 1
                print("Current Score: {}".format(score))
                

                if done:
                    print("DEAD")
                    break

            highest_score = max(highest_score, score)


        print("Final Score: {}".format(highest_score))
        self.env.close()


    # perform if you want to loop forever till you press ctrl + c:

    # def perform(self):
    #     self.model = load_model('flappymodel-138.h5')
    #     while 1:
    #         state = self.env.reset()
    #         state = np.reshape(state, [1, self.state_space])
    #         done = False
    #         score = 0

    #         while not done:
    #             self.env.render()
    #             action = np.argmax(self.model.predict(state))
    #             next_state, reward, done, info = self.env.step(action)
    #             state = np.reshape(next_state, [1, self.state_space])
    #             score += 1

    #             print("Current Score: {}".format(score))

    #             if done:
    #                 print("DEAD")
    #                 break


if __name__ == '__main__':
    agent = DeepQAgent()
    # agent.train()
    agent.perform()
    