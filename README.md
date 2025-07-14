<div align="center">
  <img height="200" src="https://raw.githubusercontent.com/LukaOliveira/inkpro-coverage/refs/heads/main/coverage.png"  />
  <h1 align="center">InkPro Coverage - Printed Coverage Calc</h1>
</div>

###

<br clear="both">

<h3 align="left">English - InkPro Coverage</h3>

###

<p align="left">InkPro Coverage calculates the printed coverage area of a PDF document. It takes a PDF and accurately displays the percentage of CMYK each page will use.</p>

###

<h4 align="left">How to install?</h4>

###

First of all, you must download and install the latest version of GhostScript. It can be found through this link: [Download GhostScript](https://github.com/ArtifexSoftware/ghostpdl-downloads/releases)

###

<p align="left">Options to run:</p>

1º Option: Access the [releases](https://github.com/LukaOliveira/inkpro-coverage/releases) page and download the version best suited to your operating system.<br><br>2º Option: Run from Python (The ideal is to create a venv)

```bash
git clone https://github.com/LukaOliveira/inkpro-coverage.git
```
```bash
cd inkpro-coverage
```
```bash
pip install -r requirements.txt
```
```bash
python main.py

```

###

<h4 align="left">Testing accuracy:</h4>
It's important to note that a 300dpi setting was used for the tests. The software supports a range from 72dpi to 1200dpi; the higher the DPI, the greater the precision.
<br><br>
Inside the "test" folder, you'll find PDF files with defined CMYK values. They should each correspond as follows:
<br>

<h5>pure_cyan.pdf</h5>
C - 100% | M - 0% | Y - 0% | K - 0%
<h5>pure_magenta.pdf</h5>
C - 0% | M - 100% | Y - 0% | K - 0%
<h5>pure_yellow.pdf</h5>
C - 0% | M - 0% | Y - 100% | K - 0%
<h5>pure_black.pdf</h5>
C - 0% | M - 0% | Y - 0% | K - 100%

###

<br clear="both">

<h3 align="left">Português (BR)- InkPro Coverage</h3>

###

<p align="left">InkPro Coverage calcula a área de cobertura impressa de um documento PDF. Ele recebe um PDF e exibe com precisão a porcentagem de CMYK que cada página utilizará.</p>

###

<h4 align="left">Como instalar?</h4>

###
Primeiro, você precisa baixar e instalar a versão mais recente do GhostScript. Ela pode ser encontrada neste link: [Download GhostScript](https://github.com/ArtifexSoftware/ghostpdl-downloads/releases)

###

Opções de execução:<br><br>1ª Opção: Acesse a página de [releases](https://github.com/LukaOliveira/inkpro-coverage/releases) e baixe a versão mais adequada ao seu sistema operacional.<br><br>2ª Opção: Execute a partir do Python (O ideal é criar um venv)

```bash
git clone https://github.com/LukaOliveira/inkpro-coverage.git
```
```bash
cd inkpro-coverage
```
```bash
pip install -r requirements.txt
```
```bash
python main.py
```
###

<h4 align="left">Testing a precisão:</h4>
É importante ressaltar de que os testes foram realizados em 300dpi. O software suporta entre 72dpi e 1200dpi; quanto maior o DPI, maior a presição.
<br><br>
Dentro da pasta "test", você irá encontrar alguns arquivos PDF com valores CMYK, eles devem corresponder aos seguintes resultados:
<br>

<h5>pure_cyan.pdf</h5>
C - 100% | M - 0% | Y - 0% | K - 0%
<h5>pure_magenta.pdf</h5>
C - 0% | M - 100% | Y - 0% | K - 0%
<h5>pure_yellow.pdf</h5>
C - 0% | M - 0% | Y - 100% | K - 0%
<h5>pure_black.pdf</h5>
C - 0% | M - 0% | Y - 0% | K - 100%