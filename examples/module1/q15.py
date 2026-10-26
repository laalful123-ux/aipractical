"""Module 1 Question 15: Write a Python program applying Bayes’ Rule to calculate the probability of disease after a positive test result using the given scenario."""

p_d=0.01; p_pos_d=0.99; p_pos_notd=0.05; p_notd=1-p_d
p_pos=p_pos_d*p_d+p_pos_notd*p_notd
p_d_pos=(p_pos_d*p_d)/p_pos
print("Probability:",p_d_pos); print("Percentage:",p_d_pos*100)
