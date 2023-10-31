A tuple is a collection of objects which ordered and immutable. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
Creating a tuple is as simple as putting different comma-separated values.

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
The empty tuple is written as two parentheses containing nothing −
tup1 = ();

ACCESSING VALUES IN TUPLES-

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup1[0]: ", tup1[0];
print "tup2[1:5]: ", tup2[1:5];

When the above code is executed, it produces the following result −

tup1[0]:  physics
tup2[1:5]:  [2, 3, 4, 5]

Updating Tuples
Tuples are immutable which means you cannot update or change the values of tuple elements.

Delete Tuple Elements
Removing individual tuple elements is not possible.

To explicitly remove an entire tuple, just use the del statement.
