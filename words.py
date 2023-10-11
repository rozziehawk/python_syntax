def print_upper_words(words, must_start_with = []):
    """
        Print words in upper case, but only if they start with the letters listed
        must_start_with uses list for now; if none provided, upper case them all
    """
    
    for word in words:
        if (len(must_start_with) > 0): # i.e. empty list, upper-case them all
            for start  in must_start_with:
                if word.startswith(start):
                    print(word.upper())
        else:
            print(word.upper())