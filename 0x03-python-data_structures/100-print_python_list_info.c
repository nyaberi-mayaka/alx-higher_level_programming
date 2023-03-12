#include <Python.h>

/**
 * print_python_list_info -  C function that prints some basic info
 * about Python lists.
 * @p: pointer to a C struct that represents a generic Python object
 * in the Python/C API
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	PyObject *item;

	/*handle error*/
	if (size == -1)
		return;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * main - initializes Python interpreter, creates an empty Python list,
 * calls the 'print_python_list_info' function to print information about
 * the list, and then deallocates the list and finishes the program.
 *
 * Return: 0
 */
int main(void)
{
	PyObject *pList;

	Py_Initialize();
	pList = PyList_New(0);

	print_python_list_info(pList);
	Py_DECREF(pList);

	return (0);
}
