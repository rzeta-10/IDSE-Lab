#CS22B1093 ROHAN G

def check(user_input):
    count = 0
    for i in user_input:
        if i == '.':
            count += 1
    return count

def output(user_input):
    if len(user_input) < 50:
        print("The length of input paragraph is less than 50, please provide the input again.")
        get_input()
        return 
    
    sentences = user_input.split('.')
    
    sentences = [sentence.strip().capitalize() for sentence in sentences if sentence.strip()]
    
    words = user_input.split()

    print(f"The total number of words present in the paragraph is: {len(words)}")
    print(f"The total number of sentences present in the paragraph is: {len(sentences)}")
    print('\n')
    for sentence in sentences:
        print(f"{sentence}.")
    
    modified_input = user_input.replace('a', 'b').replace('e', 'f').replace('i', 'j').replace('o', 'p').replace('u', 'v')
    modified_input = modified_input.replace('S', '$').replace('s', '$')
    
    print("\nModified paragraph:")
    print(modified_input)

def get_input():   
    while True:
        user_input = input("Enter the paragraph: ")
        
        sentence_count = check(user_input)
        
        if sentence_count >= 3:
            output(user_input)
            break
        else:
            print("The input paragraph does not contain a minimum of 3 sentences, please provide the input again.")

get_input()