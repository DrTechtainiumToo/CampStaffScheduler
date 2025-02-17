# Keys() vs list()
Keys() vs list() so for non printing cases where I need the keys .keys() is slightly more efficenty. But if I need it to print out i need to use list() on the keys so i dont get that weird dict_keys thing at the beginning. But overall doesn't really matter. The .keys() in pyhton 3x is a veiw object which is slightly more memory efficent. But unless bottleneck then prioritize readability. But if need .keys a bunch, easier just to create a list.

## == vs is
You use == when comparing values and is when comparing identities.
is compares two objects in memory, == compares their values.

## IN
in is a memebership operator, but also part of the for loop syntax for iteration
or combines conditional statments, and returns True if at least one of the conditions evaluates to True, and false otherwise. Returns true on first operand that is Truthy and does not eval the rest. Use to see if something in a list for example is true. DONT CONFUSE WITH AND
