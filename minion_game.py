def minion_game(string):
    vowels = 'AEIOU'
    Stuart = 0
    Kevin = 0  # words with vowels
    string_len = len(string)
    for i in range(string_len):
        if string[i] in vowels:
            Kevin += string_len - i
        else:
            Stuart += string_len - i
    final_string = f"Kevin {Kevin}" if Kevin > Stuart else f"Stuart {Stuart}" if Stuart > Kevin else "Draw"
    print(final_string)
    

if __name__ == '__main__':
    s = input()
    minion_game(s)