## Reinforcement Learning

#### Q1. Mengapa Monte Carlo adalah ide dasar dari Temporal Difference Learning?

- \[x] Monte Carlo mengevaluasi value-nya setiap episode
- \[ ] Monte Carlo tidak perlu ada termination
- \[ ] Monte Carlo adalah model free algorithm
- \[ ] Setiap episode dalam Monte Carlo tidak independent

#### Q2. Bagaimana melatih/menghitung Q-Value pada Q-Learning?

- \[ ] Melatih ANN
- \[x] Hasil perhitungan reward dan Q-Value state berikutnya
- \[ ] Hasil perhitungan return dan Q-Value state berikutnya
- \[ ] Hasil perhitungan reward demi reward

#### Q3. Perbedaan antara Control Q-Learning dengan SARSA terletak pada ...

- \[ ] Epsilon policy
- \[ ] Greedy policy
- \[ ] Eksploitasi greedy policy
- \[x] Eskploitasi policy

#### Q4. Dari pilihan berikut manakah yang benar tentang environment? 

- \[ ] Environment adalah agent
- \[ ] Environment bukan bagian dari RL
- \[x] Segala sesuatu yang menjadi tempat eksplorasi dan eksploitasi agent
- \[ ] Semua jawaban salah

#### Q5. Apa yang disebut satu episode dalam Monte Carlo?

- \[ ] Pergerakan dari satu state ke state yang lain 
- \[ ] Perpindahan state dari akhir lalu kembali ke start
- \[ ] Perpindahan dua state yang berkebalikan
- \[x] Pergerakan state dari start, ke state lain, sampai selesai

#### Q6. Di bawah ini manakah yang merupakan algoritma Dynamic Programming?

- \[ ] Policy evaluation
- \[ ] Value iteration
- \[ ] Return iteration
- \[x] Action iteration

#### Q7. Apakah fungsi reward dalam Markov Decision Process? (pilih yang paling cocok)

- \[ ] Memberikan petunjuk kepada agent dalam mengambil keputusan
- \[ ] Agar agent memilih total reward yang paling banyak
- \[x] Memberikan umpan balik kepada agen untuk mengambil keputusan 
- \[ ] Tidak ada fungsi reward dalam Markov Decision Process

#### Q8. Bagaimana bentuk robot yang seharusnya? 

- \[ ] Menyerupai manusia
- \[x] Tidak menyerupai manusia sama sekali tetapi memiliki fungsi yang menyerupai manusia
- \[ ] Menyerupai hewan seperti anjing, kucing, dll
- \[ ] Semua benar

#### Q9. Apa yang membedakan value iteration dan policy evaluation

- \[ ] Value iteration mencari policy, policy mencari value
- \[ ] Value iteration mencari policy terbaik, policy evaluation mencari value
- \[ ] Value iteration mencari policy terbaik, polocy evaluation mencari value terbaik
- \[x] Value iteration mencari value terbaik, policy evaluation mencari policy
- \[ ] Value iteration mencari value terbaik, policy evaluation mencair policy terbaik

#### Q10. Dua diantara pilihan berikut mana yang merupakan TemporalDifferenceControl adalah... 

- \[ ] Monte Carlo dan Dynamic Programming
- \[ ] Markov Decision Process dan Monte Carlo
- \[x] SARSA dan Q-Learning
- \[ ] SARSA dan Monte Carlo

#### Q11. Manakah properties yang benar?

- \[ ] State masa lalu dapat diperkirakan dari state masa depan
- \[ ] State masa lalu dapat diperkirakan dari state saat ini
- \[ ] State masa depan dapat diperkirakan dari state masa lalu
- \[x] State masa depan dapat diperkirakan dari state saat ini

#### Q12. Berikut pernyataan yang benar tentang TemporalDifferenceLearning adalah....

- \[ ] Agent belajar dari lingkungan melalui pemodelan lengkap
- \[x] Kombinasi dari Monte Carlo dan Dynamic Programming
- \[ ] Bersifat episodik dalam melakukan evaluasi value-nya
- \[ ] Tidak memiliki learning rate

#### Q13. Q-Value function memiliki input berupa.. 

- \[x] State action
- \[ ] State value
- \[ ] State return
- \[ ] Value

#### Q14. Mana yang benar tentang learning rate pada Temporal Difference Learning 

- \[ ] Semakin besar nilainya (mendekati 1) maka semakin baik dalam mencapi konvergensi
- \[x] Learning rate harus memperhatikan faktor error
- \[ ] Learning rate harus di set sekecil mungkin (mendekati 0) agar pembelajaran menjadi lebih cepat
- \[ ] Learning rate yang besar (mendekati 1) dapat meningkatkan akurasi

#### Q15. Berikut adalah pernyataan yang benar mengenai eksplorasi dan eksploitasi

- \[x] Algoritma RL yang lebih dominan eksplorasi, ada kemungkinan agent RL tersebut mendapatkan banyak peluang solusi buruk
- \[ ] Algoritma RL yang lebih dominan eksploitas, ada kemungkinan agent RL tersebut akan mendapatkan banyak peluang solusi buruk
- \[ ] Penentuan reward, baik positif maupun negatif tidak berpengaruh terhadap perilaku eksplorasi dan eksploitasi dari RL
- \[ ] Agar dapat memperbesar peluang mendapatkan solusi baik, RL bisa didorong untuk lebih dominan melakukan aksi yang berbeda (eksplorasi) dan tidak menggunakan aksi sebelumnya

#### Q16. Yang bukan merupakan komponen RL untuk robot adalah.... 

- \[ ] Reward
- \[ ] State
- \[ ] Action
- \[x] Function

#### Q17. Dalam lingkup kajian Reinforcement Learning, Monte Carlo termasuk... 

- \[ ] Model-based algorithm
- \[x] Model free algorithm
- \[ ] Reward-based algorithm
- \[ ] Environment-based algorithm

#### Q18. Apa yang dimaksud jalur (path) pada Markov Decision Process?

- \[ ] Urut urutan state yang dilalui oleh sebuah agent
- \[x] Urut urutan state dan action yang dilalui oleh sebuah agent
- \[ ] Urut urutan state, action, dan reward yang dilalui oleh sebuah agent
- \[ ] Jalur yang diambil oleh robot Markov Decision Process

#### Q19. Bagaimana perhitungan value function pada Monte Carlo untuk mengestimasi expected value? 

- \[x] Mencari nilai rata-rata returns
- \[ ] Mencari nilai rata-rata rewards
- \[ ] Total returns dilakukan dengan faktor diskon
- \[ ] Mencari nilai maksimal dari rewards

#### Q20. Dari pilihan berikut adalah elemen dari Reinforcement Learning, kecuali... 

- \[x] State
- \[ ] Policy
- \[ ] Reward Signal
- \[ ] Value Function

#### Q21. Bagaimana mendapatkan Q-value pada DQ-Learning? 

- \[ ] Melatih ANN
- \[x] Menggunakan ANN yang terlatih
- \[ ] Hasil perhitungan reward demi reward
- \[ ] Hasil perhitungan reward dan Q-value state berikutnya

#### Q22. Control SARSA terinspirasi dari... 

- \[ ] Policy evaluation
- \[x] Policy iteration
- \[ ] Artificial Neural Network 
- \[ ] Value Iteration

#### Q23. Yang merupakan ciri SARSA pada TemporalDifference Learning adalah... 

- \[x] Menggunakan action-value function
- \[ ] Update value secara episodik 
- \[ ] Menggunakan mariks probabilitas transisi
- \[ ] Tidak bootstrapping

#### Q24. Dalam lingkup kajian Reinforcement Learning, Temporal Difference Learning termasuk.... 

- \[ ] Model-based algorithm
- \[x] Model free algorithm
- \[ ] Reward-based algorithm
- \[ ] Environment-based algorithm

#### Q25. Mengapa Monte Carlo hanya untuk episodic environment?

- \[x] Karena Monte Carlo mengevaluasi value-nya setiap episode
- \[ ] Karena Monte Carlo tidak perlu ada termination
- \[ ] Karena Monte Carlo ditujukan untuk continuous environment
- \[ ] Karena setiap episode dalam Monte Carlo tidak independent