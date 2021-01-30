=======
ibans
=======

.. |package| image:: https://github.com/iltoningui/ibans-python/workflows/Python%20package/badge.svg?branch=main&style=flat

A simple yet powerfull package for validating parsing ibans

========
FEATURES
========
- Validating IBAN
    - Checks if the country suports iban
    - Validate the IBAN string size for the specific country
    - Validate the check code for countries with fix checkcode
    - Validate the structure of BBAN for the specific country
    - Validate the entire IBAN using MOD 97 operaationas decribed by ISO-7064_

    .. _ISO-7064: https://en.wikipedia.org/wiki/ISO_7064

- Parsing IBAN will get the following info
    - Country name
    - Country Alpha2 code
    - Check Code
    - Basic Bank Acount Number
    - (If Available) Bank Code
    - (If Available) Account number
    - (If Available) SWIFT
    - (If Available) Sigla
    - (If Available) Bank Name
    - (If Available) Branch code
    - (If Available) Account Type
    - (If Available) Account Holder
    - (If Available) Balance Account Number
    - (If Available) Currency Code


===========
Instalation
===========
Install using pip with::

    pip install ibans

=====
Usage
=====
Using the package is as simple as shown below

----------
Parse IBAN
----------
to parse an iban just call

.. code-block:: python

    
    >>> import ibans
    >>> iban =  ibans.parse("AO06005500009209313310152")
    >>> iban.country
    Angola
    >>> iban.country_code
    AO
    >>> iban.check_digit
    06
    >>> iban.basic_bank_account_number
    005500009209313310152
    >>> iban.bank_code
    0055
    >>> iban.account_number
    00009209313310152
    >>> iban.bank_name
    Banco Privado Atlântico, S.A.
    >>> iban.sigla
    BPA
    >>> iban.swift_bic
    PRTLAOLU
    >>> iban.branch_code
    None
    >>> iban.account_type
    None
    >>> iban.account_holder
    None
    >>> iban.balance_account_number
    None
    >>> iban.currency_code
    None

-----------
Format IBAN
-----------
Formating example

.. code-block:: python

    >>> from ibans import Iban, IbanFormat
    >>> iban =  ibans.parse("AO06 0055 0000 9209 3133 1015 2")
    >>> iban.format(IbanFormat.PRINT)      
    'AO06 0055 0000 9209 3133 1015 2'
    >>> iban.format(IbanFormat.PRINT_HIDDEN)      
    'AO06 **** **** **** **** *015 2'
    >>> iban.format(IbanFormat.ELECTRONIC)       
    'AO06005500009209313310152'

Formating example for (Belgium)

.. code-block:: python

    >>> from ibans import Iban, IbanFormat
    >>> iban =  ibans.parse("BE71096123456769")
    >>> iban.format(IbanFormat.PRINT)
    'BE71 096 1 2345 67 69'

Formating example for (Cyprus)

.. code-block:: python

    >>> from ibans import Iban, IbanFormat
    >>> iban =  ibans.parse("CY17002001280000001200527600")
    >>> iban.format(IbanFormat.PRINT)
    'CY17 002 0 0128 0000 0012 0052 7600'

============
Contributing
============

Contribuitions are welcome, please open an issue or send a PR.
Please read our Contributing and code of conduct

=======
License
=======

This project is available under MIT License

