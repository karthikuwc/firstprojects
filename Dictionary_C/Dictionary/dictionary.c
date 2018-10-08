/**
 * dictionary.c
 *
 * Computer Science 50
 * Problem Set 5
 *
 * Implements a dictionary's functionality.
 */

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdint.h>
#include <ctype.h>
#include "dictionary.h"

// Node structure defined to build a Trie
typedef struct node
{
    bool word;
    struct node * letters[27];
}node;

// Hash Table Structure (Array of Linked Lists)
typedef struct link
{
    char word[LENGTH + 1];
    struct link * next;
}link;

// Declare HashTable

link * hashtable[HASHTABLE_SIZE] = {0};


// start node - first node in trie
node root_node;


// dictionary word counter
unsigned int word_counter = 0;

// node counter
int node_counter = 0;


/**
 * Returns true if word is in dictionary else false.
 */

bool check(const char* word)
{
    // initialize cursor
    node * cursor;
    // initialize cursor to point at root
    cursor = &root_node;
    // save length of word
    int word_length = (int)strlen(word);
    
    /**
     * This loop starts with cursor pointing at root node. Corresponding index of
     * first letter of 'word' calculated then cursor updated to point to same node as
     * corresponding letters[] points to.
     *
     * When count == 0, cursor points to second node in trie. When count == word_length - 1
     * cursor points to n'th node in path, where n = word_length + 1.
     */
    for (int count = 0; count < word_length; count++)
    {
        int node_letter_index;
        
        
        if(word[count] == 39) // Accounting for apostrophe
        {
            node_letter_index = 0;
        }
        else // 96 less than ASCII value to establish 1-27 index
        {
            node_letter_index = (int)tolower(word[count]) - 96;
        }
        
        // Update cursor only if path exists in Trie
        if (cursor->letters[node_letter_index] == NULL)
        {
            cursor = &root_node;
            return false;
        }
        else
        {
            cursor = cursor->letters[node_letter_index];
        }
    }
    
    // Check if word is in dictionary by checking bool value in node
    if (cursor->word == true)
    {
        return true;
    }
    else
    {
        return false;
    }
    
}

/**
 * Loads dictionary into memory.  Returns true if successful else false.
 */
bool load(const char* dictionary)
{
    // open dictionary
    FILE * dict = fopen(dictionary, "r");
    
    if (dict == NULL)
    {
        return false;
    }
    
    // cursor
    node * cursor;
    // buffer for dictionary word being input
    int input_word[45];
    // counter for letters in word
    int letter_counter = 0;
    // buffer for letter
    char current_letter;
    // counter for letters of words assigned to nodes
    int j = 0;
    
    
    do
    {
        /**
         * This while loop loads the corresponding node index of
         * each letter of a word into an array. A letter counter
         * is used to count the number of letters in the word until
         * an EOF file character or new line chracter is reached.
         */
        do
        {
            current_letter = fgetc(dict);
            
            if (isalpha(current_letter) != 0)
            {
                input_word[letter_counter] = (int)tolower(current_letter) - 96;
                letter_counter++;
            }
            else if(current_letter == 39)
            {
                input_word[letter_counter] = 0;
                letter_counter++;
            }
        }
        while(isalpha(current_letter) != 0 || current_letter == 39);
        
        // initializing cursor
        cursor = &root_node;
        
        if(letter_counter != 0) //changed input_word to letter_counter (presuming this to check if word loaded)
        {
            
            
            // to iterate loop for only as many letters as in word
            while(j < letter_counter)
            {
                // if letter path does not yet exist
                if (cursor->letters[input_word[j]] == NULL)
                {
                    /* intialize the relevant pointer of current
                     * node to new node
                     */
                    node * new = calloc(1, sizeof(node));
                    cursor->letters[input_word[j]] = new;
                    
                    cursor = new;
                    node_counter++;
                    j++;
                    
                }
                // if letter path already exists
                else
                {
                    /* move cursor to the node which the relevant
                     * letter pointer points to
                     */
                    cursor = cursor->letters[input_word[j]];
                    j++;
                }
            }
            
            
            // removed if (feof(dict) == 0)
            
            // recording existance of word in trie
            cursor->word = true;
            
            // count word
            word_counter++;
            
            // reset cursor
            cursor = &root_node;
            
            // reset letters assigned counter
            j = 0;
            
            /** reset word buffer (code not needed)
             *for (int count = 0; count < letter_counter; count++)
             *{
             *    input_word[count] = 0;
             *}
             */
            
            // reset letters input in word counter
            letter_counter = 0;
            
        }
        
        
        
    }
    while (feof(dict) == 0);
    
    
    return true;
    
}

/**
 * Loads dictionary into memory marginally quicker than load
 * as characters are directly loaded into Trie rather than
 * through an intermediary buffer. Average time to load
 * large dictionary is 0.17.
 */
bool load2(const char* dictionary)
{
    // open dictionary
    FILE * dict = fopen(dictionary, "r");
    
    if (dict == NULL)
    {
        return false;
    }
    
    // cursor
    node * cursor;
    
    // buffer for letter
    char current_letter;
    
    // current_letter index
    int current_letter_index;
    
    do
    {
        // Initializing cursor to root_node
        cursor = &root_node;
        
        do
        {   // Read next letter in file
            current_letter = fgetc(dict);
            
            // Assign a valid letter index if letter is in alphabet or is an apostrophe,
            // else assign a flag value
            if (isalpha(current_letter) != 0)
            {
                current_letter_index = (int)tolower(current_letter) - 96;
            }
            else if(current_letter == 39)
            {
                current_letter_index = 0;
                
            }
            else
            {
                current_letter_index = 100; //Random assignment
            }
            
            // Only if valid current letter index is
            if (current_letter_index == 0 || (1 <= current_letter_index && current_letter_index <= 26))
            {
                if (cursor->letters[current_letter_index] == NULL)
                {
                    node * new = calloc(1, sizeof(node));
                    cursor->letters[current_letter_index] = new;
                    cursor = new;
                    node_counter++;
                }
                else
                {
                    cursor = cursor->letters[current_letter_index];
                }
            }
        }
        while(isalpha(current_letter) != 0 || current_letter == 39);
        
        
        // recording existance of word in trie
        cursor->word = true;
        
        // count word
        word_counter++;
        
    }
    while (feof(dict) == 0);
    
    // An extra word counted when EOF reached
    word_counter--;
    
    
    return true;
    
}

/**
 * Hashing function based on Hash table that has
 * a different bucket for every word length, first letter,
 * second letter combination.
 */
int hashing(const char * word)
{
    int index, first_letter, second_letter;
    
    first_letter  = (int)tolower(word[0]) - 96;
    
    if (strlen(word) > 1)
    {
        second_letter = (int)tolower(word[1]) - 96;
    }
    else
    {
        second_letter = 0;
    }
    
    if (strlen(word)  < 26)
    {
        index = first_letter + 26 * second_letter + 26 * 26 * (int)strlen(word);
    }
    else
    {
        index = first_letter + 26 * second_letter + 26 * 26 *  ((int)strlen(word)-26) + 26 * 26 * 26;
    }
    
    return index;
    
}


/**
 * Alternative load function that uses Hash Tables instead of Tries.
 * Average time to load dictionary is 0.10.
 */

bool load_hash(const char* dictionary)
{
    // open dictionary
    FILE * dict = fopen(dictionary, "r");
    
    if (dict == NULL)
    {
        return false;
    }
    
    // Index
    int word_index = 0;
    
    char word[LENGTH + 1] = {0};
    
    
    
    // Loop over entire file
    for (int c = fgetc(dict); c != EOF; c = fgetc(dict))
    {
        // allow only alphabetical characters and apostrophes
        if (isalpha(c) || (c == '\'' && word_index > 0))
        {
            // append character to word
            word[word_index] = c;
            word_index++;
            
         
        }
        // we must have found a whole word
        else if (index > 0)
        {
            // terminate current word
            word[word_index] = '\0';
            
            // Calculate hash of current word
            int hash = hashing(word);
            
            // Initialize new node for current word
            link * new = malloc(sizeof(link));
            
            // Assign new word to node including null terminating character
            for (int letter_counter = 0; letter_counter < strlen(word) + 1; letter_counter++)
            {
                new->word[letter_counter] = word[letter_counter];
            }
            // Make new node point to what first pointer is pointing to
            new->next = hashtable[hash];
            // Make first pointer point to new node
            hashtable[hash] = new;
            
            // update counter
            word_counter++;
            
            // prepare for next word
            word_index = 0;
            memset(word, 0, strlen(word) + 1);
        }
    }
        
    return true;

}


/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    return word_counter;
}

/**
 * Unloads dictionary from memory.  Returns true if successful else false.
 */
bool unload(void)
{
    // Initialize cursor to root_node
    node * cursor = &root_node;
    
    // To ensure every node created is freed
    while( node_counter > 0)
    {
        // For loop only ends when all letter pointers in a node return null
        for (int u = 0; u < 26; u++)
        {
            if (cursor->letters[u] != NULL)
            {
                cursor = cursor->letters[u];
                u = 0;
            }
        }
        cursor = NULL;
        free(cursor);
        node_counter--;
        cursor = &root_node;
    }
    
    return true;
}
