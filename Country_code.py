from filecmp import clear_cache
import random
import streamlit as st
import time
from streamlit import caching


st.set_page_config(layout="wide")

st.title("Welcome to the country scramble quiz")






base="dark"
primaryColor="purple"
num_countries = st.radio("Number of Countries",(5,10,15,20)) #Radio input
start_game = st.button("Start")

if 'num_countries' not in st.session_state: #Defines session state variables used throughout the code
    st.session_state.num_countries = 0

if 'show_correct' not in st.session_state:
    st.session_state.show_correct = False

if 'button_status' not in st.session_state:
    st.session_state.button_status = False

if 'answers' not in st.session_state:
    st.session_state.answers = list()

if 'add_to_avg' not in st.session_state:
    st.session_state.add_to_avg = True

if 'start_game_state' not in st.session_state:
    st.session_state.start_game_state = False

if start_game == True or st.session_state.start_game_state == True:
    st.session_state.start_game_state = True

    if num_countries != st.session_state.num_countries: # Only runs this loop if user changes radio input
        rdm_nums = [random.randrange(194) for i in range(num_countries)] #Generates random nums based on size of radio input
        st.session_state.rdm_nums = rdm_nums

    def shuffle_word(word): #Function that uses python function to shuffle a word
        word = list(word)
        random.shuffle(word)
        return ''.join(word)

    countries_file = open('list_of_countries_by_cont.txt')
    count = 0
    countries_lst_all = list()
    countries_lst_chosen = list()
    cont_lst_all = list()
    cont_lst_chosen = list()
    scrambled_lst = list()

    for line in countries_file: #Creates a list of countries and a list of continents from file input

        if (count < 98) or (count >= 145 and count <= 167) or (count >= 182):
            pos = line.find('a')
            countries_lst_all.append(line[pos+2:].rstrip())
            cont_lst_all.append(line[:pos+1])

        elif count >= 98 and count <145:
            pos = line.find('e')
            countries_lst_all.append(line[pos+2:].rstrip())
            cont_lst_all.append(line[:pos+1])

        elif count >= 169:
            pos = line.find('ia')
            countries_lst_all.append(line[pos+3:].rstrip())
            cont_lst_all.append(line[:pos+2])
        count += 1

    for i in range(num_countries):
        countries_lst_chosen.append(countries_lst_all[st.session_state.rdm_nums[i]]) #Puts the selected number of countries into a new list (randomized)
        countries_lst_chosen[i].strip() #Strips extra spaces
        countries_lst_chosen[i] = countries_lst_chosen[i].lower() #Converts beginning capital letter to lowercase so as to not give hints

        cont_lst_chosen.append(cont_lst_all[st.session_state.rdm_nums[i]])
        cont_lst_chosen[i].strip()
        cont_lst_chosen[i] = cont_lst_chosen[i].lower()


    if num_countries != st.session_state.num_countries: #Creates a 1D list only IF user changes radio input
        scrambled_lst.append([shuffle_word(country) for country in countries_lst_chosen]) #Scrambles each selected country and puts into new list
        scrambled_lst_1D = scrambled_lst[0][:] #Converts to a 1D list instead of 2D
        st.session_state.scrambled_lst_1D = scrambled_lst_1D
    st.session_state.num_countries = num_countries #This line updates the session state with current number of countries, needs to be late in code

    if 'ans1' not in st.session_state:
        st.session_state.ans1 = ' '

    ############## The below code is user output ###################

    if num_countries >= 0:
        col1a,col1b,col1c,col1d = st.columns([1.5,0.7,1,1]) #col1
        with col1a:
            st.subheader("Scrambled Countries")
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[0])
        with col1b:
            st.subheader("Continent")
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[0])
        with col1c:
            st.subheader("Unscrambled")
            ans1 = st.text_input("",key=1)
        with col1d:
            st.subheader("Correct Answer")
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[0])
        col2a,col2b,col2c,col2d = st.columns([1.5,0.7,1,1]) #col2
        with col2a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[1])
        with col2b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[1])
        with col2c:
            ans2 = st.text_input("",key=2)
        with col2d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[1])
        col3a,col3b,col3c,col3d = st.columns([1.5,0.7,1,1]) #col3
        with col3a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[2])
        with col3b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[2])
        with col3c:
            ans3 = st.text_input("",key=3)
        with col3d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[2])
        col4a,col4b,col4c,col4d = st.columns([1.5,0.7,1,1]) #col4
        with col4a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[3])
        with col4b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[3])
        with col4c:
            ans4 = st.text_input("",key=4)
        with col4d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[3])
        col5a,col5b,col5c,col5d = st.columns([1.5,0.7,1,1]) #col5
        with col5a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[4])
        with col5b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[4])
        with col5c:
            ans5 = st.text_input("",key=5)
        with col5d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[4])
    if num_countries >= 10:
        col6a,col6b,col6c,col6d = st.columns([1.5,0.7,1,1]) #col6
        with col6a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[5])
        with col6b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[5])
        with col6c:
            ans6 = st.text_input("",key=6)
        with col6d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[5])
        col7a,col7b,col7c,col7d = st.columns([1.5,0.7,1,1]) #col7
        with col7a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[6])
        with col7b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[6])
        with col7c:
            ans7 = st.text_input("",key=7)
        with col7d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[6])
        col8a,col8b,col8c,col8d = st.columns([1.5,0.7,1,1]) #col8
        with col8a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[7])
        with col8b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[7])
        with col8c:
            ans8 = st.text_input("",key=8)
        with col8d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[7])
        col9a,col9b,col9c,col9d = st.columns([1.5,0.7,1,1]) #col9
        with col9a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[8])
        with col9b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[8])
        with col9c:
            ans9 = st.text_input("",key=9)
        with col9d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[8])
        col10a,col10b,col10c,col10d = st.columns([1.5,0.7,1,1]) #col10
        with col10a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[9])
        with col10b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[9])
        with col10c:
            ans10 = st.text_input("",key=10)
        with col10d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[9])
    if num_countries >= 15:
        col11a,col11b,col11c,col11d = st.columns([1.5,0.7,1,1]) #col11
        with col11a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[10])
        with col11b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[10])
        with col11c:
            ans11 = st.text_input("",key=11)
        with col11d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[10])
        col12a,col12b,col12c,col12d = st.columns([1.5,0.7,1,1]) #col12
        with col12a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[11])
        with col12b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[11])
        with col12c:
            ans12 = st.text_input("",key=12)
        with col12d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[11])
        col13a,col13b,col13c,col13d = st.columns([1.5,0.7,1,1]) #col13
        with col13a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[12])
        with col13b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[12])
        with col13c:
            ans13 = st.text_input("",key=13)
        with col13d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[12])
        col14a,col14b,col14c,col14d = st.columns([1.5,0.7,1,1]) #col14
        with col14a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[13])
        with col14b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[13])
        with col14c:
            ans14 = st.text_input("",key=14)
        with col14d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[13])
        col15a,col15b,col15c,col15d = st.columns([1.5,0.7,1,1]) #col15
        with col15a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[14])
        with col15b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[14])
        with col15c:
            ans15 = st.text_input("",key=15)
        with col15d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[14])
    if num_countries >= 20:
        col16a,col16b,col16c,col16d = st.columns([1.5,0.7,1,1]) #col16
        with col16a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[15])
        with col16b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[15])
        with col16c:
            ans16 = st.text_input("",key=16)
        with col16d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[15])
        col17a,col17b,col17c,col17d = st.columns([1.5,0.7,1,1]) #col17
        with col17a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[16])
        with col17b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[16])
        with col17c:
            ans17 = st.text_input("",key=17)
        with col17d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[16])
        col18a,col18b,col18c,col18d = st.columns([1.5,0.7,1,1]) #col18
        with col18a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[17])
        with col18b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[17])
        with col18c:
            ans18 = st.text_input("",key=18)
        with col18d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[17])
        col19a,col19b,col19c,col19d = st.columns([1.5,0.7,1,1]) #col19
        with col19a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[18])
        with col19b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[18])
        with col19c:
            ans19 = st.text_input("",key=19)
        with col19d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[18])
        col20a,col20b,col20c,col20d = st.columns([1.5,0.7,1,1]) #col20
        with col20a:
            st.write("")
            st.write("")
            st.write("")
            st.write(st.session_state.scrambled_lst_1D[19])
        with col20b:
            st.write("")
            st.write("")
            st.write("")
            st.write(cont_lst_chosen[19])
        with col20c:
            ans20 = st.text_input("",key=20)
        with col20d:
            st.write("")
            st.write("")
            st.write("")
            if st.session_state.show_correct == True:
                st.write(st.session_state.answers[19])

    answers_lst = list()

    try:
        answers_lst.append(ans1)
        answers_lst.append(ans2)
        answers_lst.append(ans3)
        answers_lst.append(ans4)
        answers_lst.append(ans5)
        answers_lst.append(ans6)
        answers_lst.append(ans7)
        answers_lst.append(ans8)
        answers_lst.append(ans9)
        answers_lst.append(ans10)
        answers_lst.append(ans11)
        answers_lst.append(ans12)
        answers_lst.append(ans13)
        answers_lst.append(ans14)
        answers_lst.append(ans15)
        answers_lst.append(ans16)
        answers_lst.append(ans17)
        answers_lst.append(ans18)
        answers_lst.append(ans19)
        answers_lst.append(ans20)
    except:
        print("")

    button = st.button("Submit")

    if button == True or st.session_state.button_status == True: #When user presses submit, show_correct and button_status are set to true in the session state
        st.session_state.show_correct = True
        st.session_state.button_status = True
        
    if button == True or st.session_state.button_status == True: #Displays results to user if button == True in current session state
    
        count = 0
        for i in range(num_countries): #Computes how many countries the user got correct
            if answers_lst[i] in countries_lst_chosen:
                count += 1

        count_str = str(count)
        num_countries_string = str(num_countries)
        percent_score = int((count / num_countries)*100)
        percent_score_str = str(percent_score)
        output = 'You got: ' + count_str + ' out of ' + num_countries_string + ' (' + percent_score_str + '%)'
        st.header(output)

        f = open('list_of_scores.txt')
        num_score_entries=0
        all_scores = 0

        for line in f: #Loops through attached text file, computes total scores and number of entries to compute average
            all_scores += int(line)
            num_score_entries += 1

        f.close()

        average_score = int(all_scores/num_score_entries)
        output2 = 'The Average Score is: ' + str(average_score) + '%'
        st.subheader(output2)
        st.button('Show Correct Answers')
        st.session_state.answers = countries_lst_chosen

        if st.session_state.add_to_avg == True:
            f = open("list_of_scores.txt", "a")
            f.write("\n")
            f.write(percent_score_str)
            f.close()
            st.session_state.add_to_avg = False

        restart_button = st.button("Play Again")
        if restart_button:
            st.legacy_caching.clear_cache() #Clears session state
            st.experimental_rerun
