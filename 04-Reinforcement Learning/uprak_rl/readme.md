## Project Description

Ini adalah implementasi algoritma Deep Q Learning pada permainan Flappy Bird

### Prerequisites
`pip install flappy-bird-gym` <br>
`pip install keras`

### Noted
Bila ingin melakukan training pada model, jangan lupa untuk:
* uncomment kode `agent.train()`
* merubah nilai pada variable `self.episodes`
* menentukan batas minimal score sebagai kondisi terminasi untuk kemudian model disimpan: `if score >= (score yang kamu tentukan)`
<br>

Bila langsung ingin melihat performa model:
* jalankan dengan perintah `python flappybird-DQN.py`
* dapat merubah nilai pada variable `self.episodes` bila ingin eksplorasi
* atau dapat mengganti nilai range pada fungsi `perform()`
* bila ingin melihat performa model tanpa ada batasan hingga kita sendiri yang melakukan terminasi, dapat uncomment kode pada line 154 hingga 173.

**Enjoy the Code**

#### Follow my github:
* Github: https://github.com/pockypoem
* Linkedin: https://www.linkedin.com/in/jeremyas-cornelis/ 
