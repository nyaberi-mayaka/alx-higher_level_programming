#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
  Py_ssize_t size, i;
  PyObject *obj;

  if (!PyList_Check(p)) {
    printf("[*] Invalid List Object\n");
    return;
  }

  size = PyList_Size(p);
  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %ld\n", size);
  printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

  for (i = 0; i < size; i++) {
    obj = PyList_GetItem(p, i);
    printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
    if (PyBytes_Check(obj)) {
      printf("[.] bytes object info\n");
      printf("  size: %ld\n", PyBytes_Size(obj));
      printf("  trying string: %s\n", PyBytes_AsString(obj));
      printf("  first %zd bytes:", PyBytes_Size(obj) + 1);
      for (int j = 0; j < PyBytes_Size(obj) + 1; j++) {
	printf(" %02x", (unsigned char)PyBytes_AsString(obj)[j]);
      }
      printf("\n");
    }
  }
}

void print_python_bytes(PyObject *p)
{
  Py_ssize_t size, i;
  char *str;

  printf("[.] bytes object info\n");
  if (!PyBytes_Check(p)) {
    printf("  [ERROR] Invalid Bytes Object\n");
    return;
  }

  size = PyBytes_Size(p);
  str = PyBytes_AsString(p);

  printf("  size: %ld\n", size);
  printf("  trying string: %s\n", str);
  printf("  first %zd bytes:", size > 10 ? 10 : size + 1);
  for (i = 0; i < size + 1 && i < 10; i++) {
    printf(" %02x", (unsigned char)str[i]);
  }
  printf("\n");
}
