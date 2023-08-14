#include <Python.h>

/**
 * print_python_list_info - prints about python list
 * @p: A PyObject 
 */
void print_python_list_info(PyObject *p)
{
	int s, alloc, x;
	PyObject *obj;

	s = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < s; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
