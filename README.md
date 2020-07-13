# Crawler-and-pdf-parser

## Instalando:
* instalar o scrapy com "conda install -c conda-forge scrapy" ou "pip install Scrapy"

## Como usar a spider:
* iniciar um projeto scrapy com "scrapy startproject spider"
* substituir os arquivos do projeto com os do repositorio
* navegar até o diretorio do codigo pdfdownloader no terminal
* rodar o codigo com o comando "scrapy crawl (nome da spider a ser utilizada sem parenteses)"

no codigo pdfdownloader existem varias diferentes spiders para sites diferentes, cada uma delas tem uma variavel name, essa variavel é o nome para ser utilizado no comando de rodar a spider. exemplo: scrapy crawl sbcm

Repositorios de revistas:
| nome            | Instituição | Endereço |
| -----           | :-------:   | :-------:|
|opus             | ANPPOM      | [link](http://www.anppom.com.br/revista/index.php/opus/) |
|permusi          | UFMG        | [link](https://periodicos.ufmg.br/index.php/permusi/) |
|abem             | ABEM        | [link](http://www.abemeducacaomusical.com.br/revistas/revistaabem/index.php/revistaabem/) |
|Música hodie     | UFG         | [link](https://www.revistas.ufg.br/musica/) |
|orfeu            | UDESC       | [link](http://www.revistas.udesc.br/index.php/orfeu/) |
|revistamusica    | USP         | [link](https://www.revistas.usp.br/revistamusica) |
| -----           | :-------:   | :-------:|
|opus             | UFPEL       | [link](http://conservatorio.ufpel.edu.br/revista/) |
|convergências    | IPCB(PT)    | [link](http://convergencias.esart.ipcb.pt/main) |
|musicaelinguagem | UFES        | [link](http://periodicos.ufes.br/musicaelinguagem) |
|Linguagens       | FURB        | [link](http://proxy.furb.br/ojs/index.php/linguagens/index) |
|Modus            | UEMG        | [link](http://revista.uemg.br/index.php/gtic-modus/issue/archive) |
|claves           | UFES        | [link](https://periodicos.ufpb.br/ojs2/index.php/claves/index) |
|Musica           | UNB         | [link](https://periodicos.unb.br/index.php/Musica) |
|ictus            | UFBA        | [link](https://portalseer.ufba.br/index.php/ictus) |
|revista bras de m| UFRJ        | [link](https://revistas.ufrj.br/index.php/rbm) |
|em pauta         | UFRG        | [link](https://seer.ufrgs.br/EmPauta) |
|revista academica| SOUZA LIMA  | [link](https://www.faculdadesouzalima.com.br/revista-academica/) |
|musica popular   | UNICAMP     | [link](https://www.publionline.iar.unicamp.br/index.php/muspop) |
|sonora           | UNICAMP     | [link](https://www.publionline.iar.unicamp.br/index.php/sonora) |
|revista art      | UFBA        | [link](https://www.revista-art.com/) |
|vortex           | UNESPAR     | [link](http://vortex.unespar.edu.br/) |
|cognicao e artes | ABCM        | [link](http://www.abcm.ufpr.br/revista.htm) |
|Musica e cultura | ABET        | [link](http://www.abet.mus.br/musicaecultura/) |
|art cultura      | UFU         | [link](http://www.artcultura.inhis.ufu.br/) |
|rem              | UFPR        | [link](http://www.rem.ufpr.br/) |
|debates          | UNIRIO      | [link](http://www.seer.unirio.br/index.php/revistadebates/index) |
|ouvirouver       | UFU         | [link](http://www.seer.ufu.br/index.php/ouvirouver) |
|musmat           | UFRJ        | [link](https://musmat.org/musmat-journal) |
|travessias       | UNIOESTE    | [link](http://e-revista.unioeste.br/index.php/travessias/) |
|musica e educacao| ABEM        | [link](http://www.abemeducacaomusical.com.br/revistas_meb/index.php/meb) |

Repositorios de eventos:
| nome    | Endereço |
| -----   | :-------:|
|anppom   | [link](http://www.anppom.com.br/congressos/index.php/) | 
|sbcm     | [link](http://compmus.ime.usp.br/sbcm/) | 
| ------  | ----------|
| ABEM    | [link](http://www.abemeducacaomusical.com.br/revistas_meb/index.php/meb)|
| MUSMIDI | |
| ABET    | [link](http://www.abet.mus.br/#anais)|
