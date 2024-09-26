# UCI SWE240 Assignment 1 Edwin Miyatake 61346496
Task Description:

Consider a commercial bank, Bank of Orange County, where anyone can open bank accounts. To open a bank account, the following information is needed - 

- Name 
- Address
- Social Security
- An initial deposit amount. 

The bank assigns a unique ID whenever a user opens an account. The unique ID is incrementally assigned to new users, meaning if the last new user’s ID is x, the user signing up will have a unique ID (x + 1). If a user closes their account, the unique ID can be re-claimed and re-assigned to future new users. 

Task-1: Model the list of users as a linked list where each account is a node in the list. Users must be sorted by their ID in the linked list. 

Task-2: Write a method/function addUser(user) that adds a new user. Notice that the new user should have a unique ID that is either 1 more than the last unique ID or equal to the first free-up unique ID (by a user closing up their account), whichever comes first.

Task-3: Write a method/function deleteUser(ID) that deletes an existing user. Free up the unique ID while deleting the user. This unique ID can be re-assigned to a future new user.

Task-4: Write a method/function payUserToUser(payer ID, payee ID, amount) that lets the user with ID1 pay the user with ID3 by amount.

Task-5: Write a method/function getMedianID() that returns the median of all the account IDs, i.e., the middle node of the linked list. If the number of nodes is even, then you can return the average of the ids of the middle two nodes (return float), and you can also return the first middle node’s id.

Task-6: Write a method/function mergeAccounts(ID1, ID2) that merges two accounts into one. This function only merges two accounts if they are owned by the same person and identified by the same name, address, and SSN. While merging, sum the two balances, delete the account with the biggest unique ID of the two, and keep the account with the smallest unique ID with the new balance.

Task-7: Imagine another bank, Bank of Los Angeles, which has the same banking protocol and uses the same class as the Bank of Orange County. These two banks have decided to merge into a new bank, Bank of Southern California. Merge the two linked lists into one in the method mergeBanks(bankOfOrangeCounty, bankOfLosAngeles). If both lists have a node with the same ID, create a new ID for one of the duplicates and add it to the new list. While creating the new ID, you have to maintain the incremental property.
