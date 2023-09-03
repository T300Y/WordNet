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
        palindrome= ReverseString(word)
    
        IF palindrome EQUALS word THEN
            RETURN 5
        ELSE
            RETURN 1
        END IF
    END FUNCTION

#### Flow Chart
![flow chart](https://github.com/T300Y/WordNet/assets/86957414/ea3042d3-ad46-4d9e-a480-09d9d32b13e6)


#### Implementing phase
