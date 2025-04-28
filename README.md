# 📄 XML CONVERTER 
Conversor de arquivos **`XML`** para formatos **` TXT`**,**`PDF`** e **`CSV`** em **Python**

## 🎯 Objetivo:
 O **XML CONVERTER** foi desenvolvido para automatizar a conversão de arquivos no formato `.xml` para `.txt`,`.pdf` e `.csv` de forma simples e configurável. O projeto surgiu a partir da necessidade de adaptar arquivos **`XML`** a processos de importação que exigem formatos mais seguros e simplificados. Em certos ambientes corporativos, o uso direto de arquivos XML pode ser restrito por motivos de segurança ou compatibilidade, dificultando a automação de rotinas de integração de dados.

 Pensando nisso, o **XML CONVERTER** transforma arquivos **`XML`** em formatos amplamentes aceitos, viabilizando integrações automáticas e reduzindo a necessidade de intervenções manuais.


## ⚙️ Funcionalidades:
- Conversão de XML para TXT.
- Conversão de XML para PDF.
- Conversão de XML para CSV.


## 🛠 Tecnologias utilizadas:
- Python 3.13.3


## 🏗 Estrutura do Projeto:
```
xml-converter/
├── app/
│   └── main.py
├── README.md
└── requirements.txt
```


## ⚡ Como usar:
1. Instalar o Python 3.13.3
2. Instalar o `requirements.txt`

    ```
    # Clone o repositório
    git clone https://github.com/VictorPedroza/xml-converter.git

    # Acesse a pasta
    cd xml-converter

    # Instale as dependências
    pip install -r requirements.txt

    # Execute
    python src/main.py

    ```

## 🖥️ Gerando o Executável (Opcional)
```
# Instalando a Bibliteca Pyinstaller
pip install pyinstaller

# Gerando o Arquivo Executável
pyinstaller --onefile main.py

```

## 🚧 Status do projeto
- Em desenvolvimento
