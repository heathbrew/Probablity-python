"""
For the following dataset, print a sentence probabilistically. 

The system should take as input the number of words and the starting word. 
Rest the system should print a sentence on its own, i.e., you will type in 
a word and the program should tell me what the next possible word could be. 
For example, if I type the word 'We', the program should tell me that the next 
possible words could be: 1) hate 2) are 3) will 4) adore 5) watch 6)believe 
(probabistically in this order). We will call the order of words as ranking. 
Subsequently other words also.
"""
with open("Input.txt") as f:
    lines = f.readlines()
    
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")
    
    temp_array = []
    words = []
    sentence = []
    
    n = int(input())
    word = input()
    sentence.append(word)
    
    for i in lines:
        words = i.split(" ")
        for i in range(len(words)):
            if(words[i]==word):
                if(len(words[i+1:])<n):
                    continue
                else:
                    temp_array.append(words[i+1:])
    
    for i in range(n-1):
        
        sample_space = []
        unique = []
        prob = []
        for j in temp_array:
            sample_space.append(j[i])
        for k in sample_space:
            if k not in unique:
                unique.append(k)
        for j in unique:
            prob.append(sample_space.count(j)/len(sample_space))
        sentence.append(unique[prob.index(max(prob))])
        
print(" ".join(sentence))