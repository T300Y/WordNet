# WordNet
## Defining and Understanding
![context diagram](https://github.com/T300Y/WordNet/assets/86957414/df7cd8ee-bb4d-4e9e-9b30-a0cebb32a6af)


## Planning & Design phase
### Program-level planning
#### Gantt Chart
![gantt chart](https://github.com/T300Y/WordNet/assets/86957414/c5f6bd04-7b3e-4094-a7a0-d5d9a51e0578)

#### Screen Design
![screen_desing](https://github.com/T300Y/WordNet/assets/86957414/dd3cc1e7-e4c2-4d25-bd63-51802f127d66)

#### Data Dictionary

| Variable Name | Scope | Data Type | Description |
| --- | --- | --- | --- |
| WIDTH | integer | Global | Width of the Display |
| HEIGHT | integer | Global | Height of the Display |
| FPS | integer | Global | How many times the display updates and renders a new scene every second, used through pygame clock feature |
| BONUS_MESSAGE_DISPLAY | integer | Global | Integer for how many seconds the bonus message should be displayed for |
| bonus_messages | Array of strings | Global | Place the bonus message in the array, able to loop through array  for next message if messages are stacked |
| ENCOURAGEMENT_DISPLAY_DURATION | integer | Global | An integer for the amount of time the encouragement message should  be displayed for |
| encouragement_messages | Array of strings | Global | An array to store encouragement messages while one is being rendered so that all messages are displayed |
| WIN | Variable for SDL GAME ENGINE  WINDOW CREATION FUNCTION | Global | Used to render surfaces and textures and text to the screen |
| all_sprites | Group(pygame data structure) a group of one class allows methods to be used , searched like array | Global | A group data structure used to store the TextSprite class making it easy to perform group methods and finding selected sprites, adding and removing a  class from the group is simple |
| BLACK | Tuple of integers | Global | Tuple of the RGB values for black to optimise for each render |










#### Structure Chart
![IMG_2818](https://github.com/T300Y/WordNet/assets/86957414/f7957773-4bd9-4423-ad1e-5c9a94e54502)

| Variable Name | Key |
| --- | --- |
| Array of sprites | AOS |
| dictionary | DICT |
| Selected sprites array | SS |
| Selected sprite centers | SSC |
| Number of sprites | NOS  |
| Lttr array | LA |
| Valid_words | VW |
| text | T |
| Font size | FS |
| Font color | FC |
| Screen width | SW |
| Screen height | SH |
| Other sprite | OS |


### Algorithm-level planning - is_palindrome

#### Psuedocode

    BEGIN is_palindrome(word, dictionary)
        wod_length = LENGTH(word)
        palindrome = ""
        FOR i = word_length-1 TO 0 step -1
            palindrome[(word_length-1)-i] = word[i]
        IF palindrome EQUALS word THEN
            RETURN 5
        ELSE
            RETURN 1
        END IF
    END FUNCTION

#### Flow Chart
![flow chart](https://github.com/T300Y/WordNet/assets/86957414/ea3042d3-ad46-4d9e-a480-09d9d32b13e6)

#### IPO Table 

|Function Name | Input | Process | Output |
| --- | --- | --- | --- |
| is_palindrome | Word(String) and Dictionary(dictionary data class), A mutable and unordered container in python containing keys and value pairs | The inputted word is first reversed through using pythons array indexes. Whereby it loops through the string from end to front and adds it into an array. It then adds each of these array indexations back into a string and the word is reversed. It then adds this reversed word to the palindrome variable(string). It then checks if the palindrome variable is equal to the word if they are equal the program returns 5(int) which is the bonus score for having a palindrome word.Otherwise it returns 1(int) so that the bonus multiplier remains unchanged | The output is an integer either 5 or 1 as explained in the process. This is the bonus multiplier for having a palindrome word |



### Implementing phase


| Feature Name | Completed |
| --- | --- |
| letters bouncing | :heavy_check_mark: |
| lines drawn between letters of completed word | :heavy_check_mark: |
| selection of letter and add to current word | :heavy_check_mark: |
| deselection of letter and remove single instance from word | :heavy_check_mark: |
| occasionally add a new letter | :heavy_check_mark: |
| accept submitted words only if in dictionary | :heavy_check_mark: |
| remove submitted letters  only if word is in dictionary | :heavy_check_mark: |
| random feedback for positive and negative events | :heavy_check_mark: |
| Small fading message for BONUS multiplier | :heavy_check_mark: |
| Letter spawn rate adjussted to their frequency in english language | :heavy_check_mark: |
|a visible score | :heavy_check_mark: |
| base points given based on length of word(+1 point per char) | :heavy_check_mark: |
| double points for words that spell other words backwards | :heavy_check_mark: |
| 5x for words that are palindromes | :heavy_check_mark: |
| 10x for rotatable words | :heavy_check_mark: |
| +10 points for embedded words | :heavy_check_mark: |
