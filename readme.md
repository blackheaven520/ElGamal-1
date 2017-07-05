# El Gamal encryption

In cryptography, the El Gamal encryption system is an asymmetric key encryption algorithm for public-key cryptography
which is based on the Diffie–Hellman key exchange. It was described by Taher Elgamal in 1985.[1] ElGamal encryption is
used in the free GNU Privacy Guard software, recent versions of PGP, and other cryptosystems. The DSA
(Digital Signature Algorithm) is a variant of the ElGamal signature scheme, which should not be confused with
ElGamal encryption.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and
testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
PyCharm IDE
```

### Installing

A step by step series of examples that tell you have to get a development env running
is shown here : [https://www.jetbrains.com/pycharm/]



### Testing by running the program

Explain what these tests test and why

```
Prime modulus is 65537

Primitive root wrt 65537 is 3

Choose: e (encrypt) | d (decrypt) |k (get public key) | x (exit)?:
k
Please select a private key within 1 to 65537:
40000
Your Public key is:19139

########################################

Prime modulus is 65537

Primitive root wrt 65537 is 3

Choose: e (encrypt) | d (decrypt) |k (get public key) | x (exit)?:
e
Please select a number between 1 and 65537

Type secret number to send:
11
Type recipient’s public key :
19139
The encrypted secret is : (3,13918)

########################################

Prime modulus is 65537

Primitive root wrt 65537 is 3

Choose: e (encrypt) | d (decrypt) |k (get public key) | x (exit)?:
d
Type in received message in form a[space]b:

3 13918
Type in your private key:
40000
The decrypted secret is:11

########################################

Prime modulus is 65537

Primitive root wrt 65537 is 3

Choose: e (encrypt) | d (decrypt) |k (get public key) | x (exit)?:
x
########## The Program ended! ###############


Process finished with exit code 0

```




## Built With

* [Pycharm](https://www.jetbrains.com/pycharm/) - Pycharm IDE



## Authors

* **Shamveel Ahammed** - *Initial work* - (https://github.com/shamveelahammed)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


