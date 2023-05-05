## Ujian Teori Reinforcement Learning

#### Q1. Apa fungsi reward dalam Markov Decision Process? (pilih yang cocok)

- \[ ] Memberikan petunjuk kepada agent dalam mengambil keputusan
- \[ ] Agar agent memilih total reward yang paling banyak
- \[x] Memberikan umpan balik kepada agen untuk mengambil keputusan 
- \[ ] Tidak ada fungsi reward dalam Markov Decision Process

#### Q2. Dari pilihan berikut adalah elemen dari Reinforcement Learning, kecuali.... 

- \[x] State 
- \[ ] Policy
- \[ ] Reward Signal
- \[ ] Value Function

#### Q3. Apa itu return (utility) dalam Markov Decision Process? 

- \[ ] Total reward yang didapatkan oleh agent
- \[ ] Total reward yang didapatkan oleh agent berdasarkan jalur yang dilalui
- \[ ] Perkiraan total reward yang didapatkan oleh agent berdasarkan matriks probabilitas
- \[x] Perkiraan total reward yang didapatkan oleh agent berdasarkan jalur yang dilalui

#### Q4. Bagaimana melatih / menghitung Q-Value pada Q-Learning?

- \[ ] Melatih ANN
- \[x] Hasil perhitungan reward dan Q-value state berikutnya
- \[ ] Hasil perhitungan return dan Q-Value state berikutnya
- \[ ] Hasil perhitungan reward demi reward

#### Q5. Apa yang dimaksud jalur (path) pada MDP? 

- \[ ] Urut urutan state yang dilalui oleh sebuah agent
- \[ ] Urut urutan state dan action yang dilalui oleh sebuah agent 
- \[x] Urut urutan state, action, dan reward yang dilalui oleh sebuah agent
- \[ ] Jalur yang diambil oleh robot Markov Decision Process

#### Q6. Control DQ Learning terinspirasi dari... 

- \[ ] Policy evaluation
- \[ ] Policy iteration
- \[ ] Value iteration
- \[x] Gabungan Q Learning dengan ANN

#### Q7. Di bawah ini manakah Markov properties yang benar? 

- \[ ] State masa lalu dapat diperkirakan dari state masa depan 
- \[ ] State masa lalu dapat diperkirakan dari state saat ini
- \[ ] State masa depan dapat diperkirakan dari state masa lalu
- \[x] State masa depan dapat diperkirakan dari state saat ini

#### Q8. Bagaimana perhitungan value function pada Monte Carlo untuk mengestimasi expected value?

- \[x] Mencari nilai rata-rata returns
- \[ ] Mencari nilai rata-rata rewards
- \[ ] Total returns dikalikan dengan faktor diskon
- \[ ] Mencari nilai maksimal dari rewards

#### Q9. Control SARSA terinspirasi dari... 

- \[ ] Policy evaluation
- \[x] Policy iteration
- \[ ] Value iteration
- \[ ] ANN

#### Q10. Berikut pernyataan yang benar tentang Temporal Difference Learning adalah....

- \[ ] Agent belajar dari lingkungan melalui pemodelan lengkap
- \[ ] Kombinasi dari Monte Carlo dan DP
- \[x] Bersifat episodik dalam melakukan evaluasi valuenya
- \[ ] Tidak memiliki learning rate

#### Q11. Mengapa Monte Carlo adalah ide dasar dari TDL? 

- \[x] Monte Carlo mengevaluasi value-nya setiap episode
- \[ ] Monte Carlo tidak perlu ada termination
- \[ ] Monte Carlo adalah model free-algorithm
- \[ ] Setiap episode dalam Monte Carlo tidak independent

#### Q12. Q-Value function memiliki input berupa... 

- \[x] state action
- \[ ] state value
- \[ ] state return
- \[ ] value

#### Q13. Eksplorasi pada pemilihan action berguna untuk.....

- \[ ] Memilih episode terbesar dari state berikutnya
- \[ ] Memilih value terbesar dari state tersebut
- \[ ] Memilih episode terbaik dari state berikutnya
- \[x] Memilih action lain dari state tersebut

#### Q14. Bagaimana mendapatkan Q-Value pada DQ-Learning? 

- \[ ] Melatih ANN
- \[x] Menggunakan ANN yang terlatih
- \[ ] Hasil perhitungan reward demi reward
- \[ ] Hasil perhitungan reward dan Q-value state berikutnya

#### Q15. Di bawah ini manakah yang merupakan algoritme DP?

- \[ ] Policy evaluation
- \[x] Value iteration
- \[ ] Return iteration
- \[ ] Action iteration

#### Q16. Bagaimana bentuk robot yang seharusnya? 

- \[ ] Menyerupai manusia
- \[x] TIdak menyerupai manusia sama sekali tapi memiliki fungsi menyerupai manusia
- \[ ] Menyerupai hewan seperti anjing, kucing, dll
- \[ ] Semua benar

#### Q17. Dua diantara pilihan berikut mana yang merupakan Temporal Difference Control adalah....

- \[ ] Monte Carlo dan Dynamic Programming
- \[ ] Markov Decision Process dan Monte Carlo
- \[x] SARSA dan Q-learning
- \[ ] SARSA dan Monte Carlo

#### Q18. Perbedaan antara control Q-Learning dengan SARSA terletak pada.... 

- \[ ] Epsilon policy
- \[x] Greedy policy
- \[ ] Eksploitasi greedy policy
- \[ ] Eksploitasi policy

#### Q19. Dalam lingkup kajian RL, Monte Carlo termasuk...

- \[ ] Model-based algorithm
- \[x] Model-free algorithm
- \[ ] Reward-based algorithm
- \[ ] Environment-based algorithm

#### Q20. Berikut adalah pernyataan yang benar mengenai eksplorasi dan eksploitasi

- \[x] Algoritma RL yang lebih dominan eksplorasi, ada kemungkinan agent RL tersebut mendapatkan banyak peluang solusi buruk
- \[ ] Algoritma RL yang lebih dominan eksploitas, ada kemungkinan agent RL tersebut akan mendapatkan banyak peluang solusi buruk
- \[ ] Penentuan reward, baik positif maupun negatif tidak berpengaruh terhadap perilaku eksplorasi dan eksploitasi dari RL
- \[ ] Agar dapat memperbesar peluang mendapatkan solusi baik, RL bisa didorong untuk lebih dominan melakukan aksi yang berbeda (eksplorasi) dan tidak menggunakan aksi sebelumnya

#### Q21. Manakah yang merupakan ciri-ciri RL? 

- \[ ] Membutuhkan data kebenaran untuk melakukan pembelajaran
- \[ ] Mengelompokkan data berdasarkan ciri-ciri atau fiturnya
- \[x] Berinteraksi dengan lingkungan dapat membuat agent semakin cerdas
- \[ ] Benar semua

#### Q22.Mengapa Monte Carlo hanya untuk episodic environment? 

- \[x] Karena Monte Carlo mengevaluasi value-nya setiap episode
- \[ ] Karena Monte Carlo tidak perlu ada termination
- \[ ] Karena Monte Carlo ditujukan untuk continuous environment
- \[ ] Karena setiap episode dalam Monte Carlo tidak independent

#### Q23. Q-Value function memiliki output berupa.... 

- \[ ] State
- \[x] Value
- \[ ] State return 
- \[ ] State value

#### Q24. Manakah komponen penyusun model Reinforcement Learning? 

- \[ ] Branch
- \[x] Environment
- \[ ] Leaf
- \[ ] Fuzzy

#### Q25. Dari pilihan berikut, manakah yang benar tentang enviroment?

- \[ ] Environment adalah agent
- \[ ] Environment bukan bagian dari Reinforcement Learning
- \[x] Segala sesuatu yang menjadi tempat eksploitasi dan eksplorasi agent
- \[ ] Salah semua