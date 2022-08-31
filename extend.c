#define PY_SSIZE_T_CLEAN
//#include "/Users/brendontoyama/opt/anaconda3/include/python3.8/Python.h"
#include <Python.h>


static PyObject *extend(PyObject *self, PyObject *args)
{
    const int *choice;
    int answer = 0;

    if (!PyArg_ParseTuple(args, "i", &choice))
        // if false we return NULL
        return NULL;

    return PyLong_FromLong(answer);
}

static PyMethodDef extendMethods[] = {
    {"extend", extend, METH_VARARGS, "extend test"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef extendmodule = {
    PyModuleDef_HEAD_INIT,
    "extend",
    "extend test",
    -1,
    extendMethods
};

// when a python program imports your module for the first time it will call PyInit_rps()
PyMODINIT_FUNC PyInit_extend(void) {
    return PyModule_Create(&extendmodule);
}