#include "hash_tables.h"

/*
 * key_index: function gives index of key
 * @key: key string.
 * @size: size of arr
 * Return: the index
 */

unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	unsigned long int hash_value = hash_djb2(key);
	unsigned long int index = hash_value % size;

	return (index);
}
