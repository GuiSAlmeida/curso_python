# Programação Orientada a Objetos com Python

## 1. Introdução
Python se difere bastante de outras linguagens de programação que tem suporte, ou que são totalmente voltadas a orientação a objetos.  
Por isso resovi criar este pequeno guia com alguns detalhes da linguagem voltados para programação orientada a objetos.

### 1.1. Convenções de nomes em Python  
Essas convenções tem um nome que podemos usar para nos referir ao modo como estamos nomeando determinados objetos em nosso programa:

**PascalCase** - significa que todas as palavras iniciam com letra maiúscula e nada é usado para separá-las, como em: `MinhaClasse`, `Classe`, `MeuObjeto`, `MeuProgramaMuitoLegal`.  
Essa á a convenção utilizada para **classes** em Python;

**camelCase** - a única diferença de camelCase para PascalCase é a primeira letra. Em camelCase a primeira letra sempre será minúscula e o restante das palavras deverá iniciar com letra maiúscula. Como em: `minhaFuncao`, `funcaoDeSoma`, etc...  
Essa conversão **não é usada** em Python;

**snake_case** - este é o padrão usado em Python para definir qualquer coisa que não for uma classe.  
Todas as letras serão minúsculas e separadas por um underline, como em: `minha_variavel`, `funcao_legal`, `soma`.

**Portanto os padrões usados em Python são:**  
`snake_case` para qualquer coisa e `PascalCase` para classes.

## 2. Classes
Classes proporcionam uma forma de organizar dados e funcionalidades juntos. Criar uma nova classe cria um novo “tipo” de objeto, permitindo que novas “instâncias” desse tipo sejam produzidas. Cada instância da classe pode ter atributos anexados a ela, para manter seu estado. Instâncias da classe também podem ter métodos (definidos pela classe) para modificar seu estado.
### 2.1. Declarar classe
```python
class Pessoa:
    pass
```

### 2.2. Classe Abstrata
Classe genérica que não vai ser estanciada, pode ter métodos concretos e abstratos.
Para isso devemos importar o módulo abc (abstract base class).
```python
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self):
        pass

class B(A):
    def falar(self):
        print(f'B Falando...')

abst = B()
abst.falar()
```

### 2.3. Atributos
Os atributos podem ser definidos direto dentro da classe **(Atributo de Classe)** 
ou dentro dos métodos criados na classe **(Atributos da Instância)**.  

A diferença é que o atributo da classe pode ser acessado e alterado pela classe 
mas as instâncias só podem acessá-lo mas não conseguem alterá-lo.

Caso a instância atribua um novo valor para o atributo de mesmo nome que herdou da classe 
acabará por criar um novo atributo de instância enquanto o atributo da classe permanece inalterado.  

```python
class Cls:
    num = 1

inst = Cls()
print(inst.__dict__)
# {} (o objeto ainda não possui nenhum atributo de instância...)
print(inst.num)
# 1 (e como não possui o atributo "num" recorre um nivel acima onde encontra o atributo da classe...)
inst.num = 2
print(inst.__dict__)
# {'num': 2} (depois da atribuição agora o objeto possui seu próprio atributo...)
print(inst.num)
# 2 (então não acessa mais o atributo de mesmo nome da classe...)
print(Cls.num)
# 1 (onde o atributo ainda possui valor inicial.)
```

### 2.4. Métodos
#### 2.4.1. Métodos de instância
Qualquer método criado dentro da classe, ao instanciar um objeto pela classe vai receber esses métodos dela.

##### `self`
Todos **métodos de instância** da classe recebem como primeiro atributo o `self`, 
ele refere-se a instancia que foi criada a partir da classe.

```python
class Pessoa:
    def comer(self, alimento):
        print(f'Pessoa está comendo {alimento}.')
```

Atributos da classe podem ser declarados no construtor sendo atribuidos os valores que forem passados por parâmetro,
como também serem criados diretos na classe sendo acessiveis para todas instancias criadas através do self.

#### 2.4.2. Métodos da classe
Além dos **métodos de instância** que ficam disponiveis para cada objeto instanciado a partir da classe, 
também podem ser criados métodos próprios da classe onde ficam acessiveis apenas para a classe em si 
e não para objetos instanciados a partir da classe.
Para esse comportamento devemos passar antes um decorator chamado `@classmethod` e o primeiro parâmetro passa a ser a própria classe `(cls)`.
```python
class Pessoa:
    ano_atual = 2021
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def pessoa_nasc(cls, nome, nasc):
        idade = cls.ano_atual - nasc
        return cls(nome, idade)
```

#### 2.4.3. Métodos estáticos
São métodos que **não recebem** o contexto da instância e da classe, 
poderiam até ser criados fora da classe, mas se necessário podem ser criados dentro da classe.  
Deve-se adicionar um decorator `@staticmethod` antes da assinatura do método.
```python
from random import randint
class Pessoa:    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand
```

#### 2.4.3. Métodos abstratos
São métodos que **não possuem** um corpo apenas a assinatura do método, 
geralmente são criados dentro de uma classe abstrata para serem sobrescritos 
nos instâncias que herdarem dessa classe.  

```python
from abc import ABC, abstractmethod
class Example(ABC):    
    @abstractmethod
    def sacar(self, valor):
        pass
```

#### 2.4.4. Métodos "mágicos"
São métodos especiais que você pode definir para adicionar "magia" às classes. 
Eles estão sempre cercados por dois underlines (por exemplo, `__init__` ou `__lt__`).  
Para ver todos métodos mágicos recomendo este [guia](https://rszalski.github.io/magicmethods/), 
seguem alguns mais usados:

##### `__new__`
É o primeiro método a ser chamado na instanciação de um objeto. 
Ele recebe a classe e, a seguir, quaisquer outros argumentos e passará para o `__init__`.
.
```python
class Pessoa:
    def __new__(cls, *args, **kwargs):
        pass
```

##### `__init__`
O inicializador da classe, é chamado assim que a classe for instanciada.
```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
```

##### `__call__`
Permite que uma instância de uma classe seja chamada como uma função. 
Essencialmente, isso significa que `Pessoa()` é o mesmo que `Pessoa.__call__()`. 
Observe que `__call__` leva um número variável de argumentos, 
isso significa que você define `__call__` como faria com qualquer outra função, 
usando quantos argumentos quiser.  

```python
class Pessoa:
    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)

p = Pessoa()
p(1, 2, 3, nome='Gui')
# (1, 2, 3)
# {'nome': 'Gui'}
```
##### `__setattr__`
É uma solução de **encapsulamento**. Ele permite que você defina o comportamento para atribuição a um atributo, 
independentemente da existência ou não desse atributo, 
o que significa que você pode definir regras personalizadas para quaisquer alterações nos valores dos atributos.

```python
class Pessoa:
    def __init__(self, name):
        self.name = name
        
    def __setattr__(self, key, value):
        if key != 'name':
            self.__dict__[key] = value
        print(key, value)
```
### 2.5. Metaclasses
Em Python tudo é um objeto, incluindo classes. Metaclasses são as "classes" que criam classes.  
`type` é uma metaclasse também.

```python
# type(name = nome da classe, bases = classes herdadas, namespace = atributos e métodos)
M = type('metaclasse', (), {})  

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_cls' in namespace:
            del namespace['attr_cls']

        return type.__new__(mcs, name, bases, namespace)
```

### 2.6. Enum (Python 3.4)
Enum é uma classe em python para a criação de **enumerações**, 
que são um conjunto de nomes simbólicos (membros) 
vinculados a valores constantes e únicos. Os membros de uma enumeração 
podem ser comparados por esses nomes simbólicos, 
e a própria enumeração pode ser iterada. Um enum tem as seguintes características.  
- Os enums são representações de string avaliadas de um objeto também chamado `repr()`.
- O nome do enum é exibido usando a palavra-chave `name`.
- Usando `type()`, podemos verificar os tipos de enum.  

```python
from enum import Enum

class Directions(Enum):
    right = 0
    left = 1
    up = 2
    down = 3

def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name} to position {direction.value}'
```

## 3. Polimorfismo
Em python o **único polimorfismo que a linguagem suporta** é por sobreposição,
que é o princípio que permite que classes derivadas de uma mesma superclasse 
tenham métodos iguais (de mesma assinatura) mas comportamentos diferentes. 
Mesma assinatura = Mesma quantidade e tipo de parâmetros.

```python
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, msg):
        pass

class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')

class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')

b = B()
c = C()
b.fala('de Skate')
# B está falando de Skate
c.fala('de futebol')
# C está falando de futebol
```

## 4. Encapsulamento
O encapsulamento é um dos pilares da orientação a objetos. Serve para proteger dados da classe. 
Encapsular os dados de uma aplicação significa evitar que estes sofram acessos indevidos.  
Para isso, é criada uma estrutura onde são usados modificadores como `public, protected, private` para restringir a acesso a esses dados.  
E métodos que podem ser utilizados por qualquer outra classe, sem causar inconsistências no desenvolvimento comumente chamados **getters e setters**.  

### 4.1. Getters & Setters
Esses métodos são chamados logo que um objeto é instanciado a partir da classe, servem como um **filtro**.  

O método `getter` obtém um valor para o atributo da instância. 
E deve conter o decorador `@property` antes de sua assinatura.  

O método `setter` configura um valor para o atributo. 
Deve conter um decorador com mesmo nome do atributo seguido de setter.
Por convenção deve-se retornar o atributo com um _ atrás.

```python
class Produto:    
    def __init__(self, nome):
        self.nome = nome
    
    # Getter
    @property
    def nome(self):
        return self._nome

    # Setter
    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

```

### 4.2. Modificadores

Em python **não temos modificadores** para restringir o acesso a dados da classe. 
Portanto ao nomear atributos e métodos segue-se uma **convenção** da PEP8:  
```properties
nome = public
_nome = protected
__nome = private
```

Na prática os atributos ou métodos ainda podem ser acessados e modificados, 
o que muda é que quando criado com `__` o python não deixa ser reatribuido valor 
para essa variável, ele acaba criando outra com mesmo nome na instância: `obj.__nome`. 
E para acessar o valor da variavel original deve colocar o nome da classe antes: `obj._Classe__nome`.

**Exemplo:**
```python
class Dados:
    def __init__(self):
        self.publicos = {}
        self._protegidos = {}
        self.__privados = {}

    # getter para obter valor fora da classe/objeto
    @property
    def protegidos(self):
        return self._protegidos

    # setter para setar valor fora da classe/objeto
    @protegidos.setter
    def protegidos(self, valor):
        self._protegidos = valor
```

### 4.3. Type Hints (Python 3.5)
Python possui tipagem dinâmica, onde os tipos são verificados durante a execução. 
E também tipagem forte, todas as operações entre tipos diferentes devem ser explicitamente definidas 
e operações não definidas entre tipos vão resultar em um erro.  
Para isso o uso dos type hints pode ser de grande auxílio para programadores com background 
em alguma linguagem estaticamente tipada como Java, Haskell e Go que tenha que 
desenvolver algo maior do que um simples script em Python.  
Muitas são as vantagens de seu uso como:
- Servem como uma forma de documentação;
- Otimizações em tempo de compilação;
- Segurança ao analizar o programa;
- Code-complete melhor;
- É mais fácil de se achar em uma codebase extensa.

Exemplos:
```python
from typing import Union

# Definindo tipos de variáveis
x: int = 10
y: float = 10.5
z: bool = False

# Definindo tipos de argumentos e retorno de uma função
def greeting(name: str) -> str:
    return 'Hello ' + name

# Definindo retorno com mais de um tipo com Union do módulo typing
def fn(p1: float, p2: int) -> Union[int, float]:
    return p1 * p2
```

## 5. Relações entre classes

- Associação (Usa outra classe)
- Agregação (Tem outra classe)
- Composição (É dono de outra classe)
- Herança (É outra classe)

### 5.1. Associação
Ela descreve um vínculo que ocorre entre classes.  
A forma mais comum de implementar associação é ter um objeto como atributo de outro, neste exemplo, abaixo:

```python
class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta
        

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')
        
    
escritor = Escritor('João')
caneta = Caneta('Bic')

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
```
### 5.2. Agregação
É um tipo especial de associação onde tenta-se demonstrar que as informações de um objeto (chamado objeto-todo) 
precisam ser complementados pelas informações contidas em um ou mais objetos de outra classe (chamados objetos-parte) 
conhecemos como **todo/parte**. Porém essas partes podem existir separadamente.  

Neste exemplo de agregação os classes podem existir separadamente porém funcionam melhor quando o carrinho possui produtos.
```python
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class CarrinhoCompras:
    def __init__(self, ):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(f'{produto.nome}: R${produto.valor}')

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return f'R${total}'
    
    
carrinho = CarrinhoCompras()
p1 = Produto('Bone', 50)
p2 = Produto('cueca', 20)
p3 = Produto('tenis', 150)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.lista_produtos()
# Bone: R$50
# cueca: R$20
# tenis: R$150
print(carrinho.soma_total())
# R$220
```

### 5.3. Composição  
Uma composição tenta representar também uma relação todo/parte. 
No entanto, na composição o objeto-todo é responsável por criar e destruir suas partes. 
Em uma composição um mesmo objeto-parte não pode se associar a mais de um objeto-todo.  

No exemplo abaixo, o objeto cliente possui um objeto endereço na sua lista de endereços, nesse caso quando o objeto cliente que é o objeto-todo for excluido,
o objeto endereço também será.
```python
class Cliente:
    def __init__(self, nome):
        self.__nome = nome
        self.__enderecos = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def inseri_endereco(self, cidade):
        self.__enderecos.append(Endereco(cidade))

    def lista_enderecos(self):
        for endereco in self.__enderecos:
            print(endereco.cidade)

class Endereco:
    def __init__(self, cidade):
        self.__cidade = cidade

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

cliente1 = Cliente('João')
cliente1.inseri_endereco('Florianópolis')
print(cliente1.nome)
# João
cliente1.lista_enderecos()
# Florianópolis
del cliente1
```

### 5.4. Herança 
Um objeto pode ter métodos e atributos de outra classe por herança, 
isso significa que a classe tem todas caracteristicas da classe herdada, 
além de poder ter as suas próprias também.  

Uma das grandes vantagens de usar o recurso da herança é na reutilização do código. 
Esse reaproveitamento pode ser acionado quando se identifica que o atributo ou método de uma classe será igual para as outras. 
Para efetuar uma herança de uma classe é passado o nome da classe como parâmetro.  

```python
# superclasse
class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def falar(self):
        print(f'{self.nome} está falando...')


# subclasses
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} estudando...')
```

#### 5.4.1. Sobreposição de métodos
Métodos herdados podem ser sobrescritos dentro da classe.  
Para usar a lógica do método sobrescrito e adicionar mais linhas de código é necessário passar ao método `super()` 
que se refere a classe que está sendo herdada, para referenciar uma classe especifica dentro da cadeia de herança 
é necessário passar o nome da classe com o método e por parâmetro o `self`.  

```python
class ClienteVip(Cliente):
    def __init__(self, nome, sobrenome):
        super().__init__(nome)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)  # neste caso se refere a classe Pessoa especificamente.
        super().falar()     # neste caso se refere a classe herdada (Cliente).
        print(f'{self.nome} {self.sobrenome} é vip...')
```

#### 5.4.2. Herança multipla
Herança múltipla, em orientação a objetos, é o conceito de herança de duas ou mais classes.

```python
class A:
    def falar(self):
        print('Falando... Estou em A.')

class B(A):
    def falar(self):
        print('Falando... Estou em B.')

class C(B, A):
    pass

c = C()
c.falar()
# Falando... Estou em B.
```

#### 5.4.3. Mixin
Especialmente no contexto do Python, um **mixin** é uma classe pai que fornece funcionalidade às subclasses, **mas não se destina a ser instanciado**.
```python
class LogMixin:
    """
    cria um arquivo de log com infos e errors.
    """
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        """
        grava mensagem de info no arquivo
        :param msg:
        :return:
        """
        self.write(f'INFO: {msg}')


    def log_error(self, msg):
        """
        grava mensagem de erro no arquivo
        :param msg:
        :return:
        """
        self.write(f'ERROR: {msg}')
```

## 6. Referências
- https://www.udemy.com/course/python-3-do-zero-ao-avancado/
- https://docs.python.org/pt-br/3/tutorial/
- https://www.codigofluente.com.br/aula-15-python-orientacao-a-objeto-01/
- https://rszalski.github.io/magicmethods/
- https://docs.python.org/3/library/typing.html
- https://diogommartins.medium.com/python-3-e-type-hints-40e80a9e8214
