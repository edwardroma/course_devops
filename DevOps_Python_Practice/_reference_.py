"""Naming Conventions"""
# Names visible as public parts of the API
# should reflect usage rather than implementation.
""" VARIABLE """
""" CONSTANT """
""" FUNCTION """
""" MODULE   """
""" CLASS    """
""" CLASS ATTRIBUTE """

"""GENERAL Naming Styles"""
b = "single lowercase letter"
B = "single uppercase letter"
bb = "lowercase"
bb_bbb = "lower_case_with_underscores"
BB = "UPPERCASE"
BB_BBB = "UPPER_CASE_WITH_UNDERSCORES"
BbBbb = "CapitalizedWords, or CapWords, or CamelCase, or StudlyCaps"
# Note: When using acronyms in CapWords, capitalize all the letters
# of the acronym. Thus, HTTPServerError is better than HttpServerError.
bbBbb = "mixedCase (differs from CapitalizedWords by initial lowercase)"
Bbbb_Bbbb_Bbbb = "Capitalized_Words_With_Underscores (ugly!)"
bb_bbb_list = ["bbb_1", "bbb_2", "bbb_3"]
# Using a short unique prefix to group related names together.
# Rare in Python. E.g.: os.stat() function returns a tuple
# whose items traditionally have names like st_mode, st_size, st_mtime, etc.
# This is done to emphasize the correspondence with the fields
# of the POSIX system call struct.
_bb_bbb_bbbb = "_single_leading_underscore"
# weak “internal use” indicator. E.g. 'from M import *' does not import objects
# whose names start with an underscore.
bb_bbb_bbb_ = "single_trailing_underscore_"
# used by convention to avoid conflicts with Python keyword, e.g. :
# tkinter.Toplevel(master, class_='ClassName')

__bb_bbb_bbb = "__double_leading_underscore"
# when naming a class attribute, invokes name mangling
# (inside class FooBar, __boo becomes _FooBar__boo; see below).
__bb_bb_bb__ = "__double_leading_and_trailing_underscore__"
# “magic” objects or attributes that live in user-controlled namespaces.
# E.g. __init__, __import__ or __file__. Never invent such names;
# only use them as documented.

"""Names to Avoid as single character variable names: 
--- ‘l’ (lowercase letter el), 
--- ‘O’ (uppercase letter oh), or 
--- ‘I’ (uppercase letter eye) 
As in some fonts, they are indistinguishable from the numerals one and zero. 
When tempted to use ‘l’, use ‘L’ instead."""

""" ASCII Compatibility
Identifiers used in the standard library must be ASCII compatible 
as described in the policy section of PEP 3131."""

""" Modules / Packages should have names:
--- short, 
--- all-lowercase names
--- Underscores can be used to improve readability
When an extension module written in C or C++ has an accompanying Python module 
that provides a higher level (e.g. more object oriented) interface, 
the C/C++ module has a leading underscore (e.g. _socket)."""

""" Class names should normally use the 
--- CapWords convention for non-callables.
--- Function's convention for callables."""

# Note that there is a separate convention for builtin names:
# most builtin names are single words (or two words run together),
# with the CapWords convention used only for exception names and builtin constants.

# Type Variable Names.
# Names of type variables introduced in PEP 484 should normally use CapWords
# preferring short names: T, AnyStr, Num. It is recommended to add suffixes
# _co or _contra to the variables used to declare covariant or contravariant
# behavior correspondingly:

from typing import TypeVar
VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)

"""Exception Names
--- As exceptions should be classes, the class naming convention applies here.
--- Still, if the exception is an error, use the suffix “Error” on exception names."""

"""Global Variable Names"""
# for use inside one module only - the same as for functions.

# Modules that are designed for use via 'from M import *' should use the
# __all__ mechanism to prevent exporting globals, or use the older convention of
# prefixing such globals with an underscore (which you might want to do to indicate
# these globals are “module non-public”).

"""Function and Variable names should be:"""
# --- lowercase,
# --- with words separated by underscores as necessary to improve readability.

# mixedCase is allowed only in contexts where that’s already the prevailing style
# (e.g. threading.py), to retain backwards compatibility.

"""Function and Method Arguments"""
# ALWAYS !!!
# use 'self' for the first argument to instance methods.
# use "cls" for the first argument to class methods.

"""If a function argument’s name clashes with a reserved keyword"""
# BAD - 'clss' - don't use an abbreviation or spelling corruption.
# GOOD - 'class_' - append a single trailing underscore
# BEST - 'class_instance' - avoid clashes by using a synonym.

"""Method Names and Instance Variables"""
# Use the function naming rules:

# Use one leading underscore only for non-public methods and instance variables.
#
# To avoid name clashes with subclasses, use two leading underscores to invoke
# Python’s name mangling rules.
#
# Python mangles these names with the class name: if class Foo has an attribute
# named __a, it cannot be accessed by Foo.__a. (An insistent user could still
# gain access by calling Foo._Foo__a.) Generally, double leading underscores
# should be used only to avoid name conflicts with attributes in classes
#     designed to be subclassed.
#
# Note: there is some controversy about the use of __names (see below).

"""Constants"""
#
# Constants are usually defined on a module level and written in all
# capital letters with underscores separating words. Examples include
# MAX_OVERFLOW and TOTAL.
#
# Designing for Inheritance
#
# Always decide whether a class’s methods and instance variables
# (collectively: “attributes”) should be public or non-public. If
# in doubt, choose non-public; it’s easier to make it public later
# than to make a public attribute non-public.
#
# Public attributes are those that you expect unrelated clients of your
# class to use, with your commitment to avoid backwards incompatible
# changes. Non-public attributes are those that are not intended to be
# used by third parties; you make no guarantees that non-public attributes
# won’t change or even be removed.
#
# We don’t use the term “private” here, since no attribute is really private
# in Python (without a generally unnecessary amount of work).
#
# Another category of attributes are those that are part of the
# “subclass API” (often called “protected” in other languages). Some
# classes are designed to be inherited from, either to extend or modify
# aspects of the class’s behavior. When designing such a class, take care to
# make explicit decisions about which attributes are public, which are part
# of the subclass API, and which are truly only to be used by your base class.
#
# With this in mind, here are the Pythonic guidelines:
#
# Public attributes should have no leading underscores.
# If your public attribute name collides with a reserved keyword,
# append a single trailing underscore to your attribute name.
# This is preferable to an abbreviation or corrupted spelling.
# (However, notwithstanding this rule, ‘cls’ is the preferred
# spelling for any variable or argument which is known to be a
# class, especially the first argument to a class method.)
# Note 1: See the argument name recommendation above for class methods.
#
# For simple public data attributes, it is best to expose just the attribute
# name, without complicated accessor/mutator methods. Keep in mind that
# Python provides an easy path to future enhancement, should you find that
# a simple data attribute needs to grow functional behavior. In that case, use
# properties to hide functional implementation behind simple data attribute
# access syntax.
# Note 1: Try to keep the functional behavior side-effect free, although
# side-effects such as caching are generally fine.
# Note 2: Avoid using properties for computationally expensive operations;
# the attribute notation makes the caller believe that access is (relatively) cheap.
#
# If your class is intended to be subclassed, and you have attributes that
# you do not want subclasses to use, consider naming them with double
# leading underscores and no trailing underscores. This invokes Python’s
# name mangling algorithm, where the name of the class is mangled into the
# attribute name. This helps avoid attribute name collisions should subclasses
# inadvertently contain attributes with the same name.
# Note 1: Note that only the simple class name is used in the mangled name, so
# if a subclass chooses both the same class name and attribute name, you
# can still get name collisions.
# Note 2: Name mangling can make certain uses, such as debugging and
# __getattr__(), less convenient. However the name mangling algorithm is well
# documented and easy to perform manually.
# Note 3: Not everyone likes name mangling. Try to balance the need to avoid
# accidental name clashes with potential use by advanced callers.

"""Public and Internal Interfaces"""
#
# Any backwards compatibility guarantees apply only to public interfaces.
# Accordingly, it is important that users be able to clearly distinguish
# between public and internal interfaces.
#
# Documented interfaces are considered public, unless the documentation
# explicitly declares them to be provisional or internal interfaces exempt
# from the usual backwards compatibility guarantees. All undocumented
# interfaces should be assumed to be internal.
#
# To better support introspection, modules should explicitly declare the names
# in their public API using the __all__ attribute. Setting __all__ to an empty list
# indicates that the module has no public API.
#
# Even with __all__ set appropriately, internal interfaces (packages, modules,
# classes, functions, attributes or other names) should still be prefixed with
# a single leading underscore.
#
# An interface is also considered internal if any containing namespace (package
# , module or class) is considered internal.
#
# Imported names should always be considered an implementation detail. Other modules
# must not rely on indirect access to such imported names unless they are an
# explicitly documented part of the containing module’s API, such as os.path or
# a package’s __init__ module that exposes functionality from submodules.
# Programming Recommendations
#
#     Code should be written in a way that does not disadvantage other
#     implementations of Python (PyPy, Jython, IronPython, Cython, Psyco, and such).
#
#     For example, do not rely on CPython’s efficient implementation of
#     in-place string concatenation for statements in the form a += b or
#     a = a + b. This optimization is fragile even in CPython (it only
#     works for some types) and isn’t present at all in implementations that
#     don’t use refcounting. In performance sensitive parts of the library,
#     the ''.join() form should be used instead. This will ensure that concatenation
#     occurs in linear time across various implementations.
#     Comparisons to singletons like None should always be done with is or is
#     not, never the equality operators.
#
#     Also, beware of writing if x when you really mean if x is not None – e.g.
#     when testing whether a variable or argument that defaults to None was set
#     to some other value. The other value might have a type (such as a container
#     ) that could be false in a boolean context!
#     Use is not operator rather than not ... is. While both expressions are
#     functionally identical, the former is more readable and preferred:
