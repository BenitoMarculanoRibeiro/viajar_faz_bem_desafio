# viajar_faz_bem_desafio

## Requisitos

* Windows 10
* Python 3.8.10
* Django==4.0.4

## Rodando o projeto

1. Clone o projeto.
2. ```
   python -m pip install virtualenv env
   ```
3. ```
   python -m virtualenv env
   ```
4. ```
   .\env\Scripts\activate.bat
   ```
5. ```
   pip install -r requirements.txt
   ```
6. ```
   python manage.py runserver
   ```

   Nesse ponto o servidor já estará rodando na url: http://127.0.0.1:8000/ porem não estará funcionando.
7. ```
   python manage.py makemigrations vitrines  
   python manage.py sqlmigrate vitrines 0001 
   python manage.py migrate

   ```

   Nesse ponto já estará funcionando, entretanto não terá nenhum dado.
8. ```
   python popula.py
   python concerta_images.py
   ```
9. Aqui já estará funcionando e com dados mas não podera acessar a parte de administração do site com o comando `py manage.py createsuperuser` será possivel criar um super usuario para poder acessar o sistema de administração do site.
10. Pode ser usado o programa ngrok para criar um servidor na propria maquina, mas terá que adicionar o link gerado em ALLOWED_HOSTS no arquivo desafio/settings.py, ficando algo como `ALLOWED_HOSTS = ['2c13-177-71-45-63.sa.ngrok.io', '127.0.0.1']` e lembresse de manter o host `'127.0.0.1'` para poder rodar localmente.
11. A para acessar o site deverá entrar `http://127.0.0.1:8000/vitrines/` ou `http://127.0.0.1:8000/admin/` para entrar na área de admin do site.

## Rotas

##### vitrines/

Mostra todas as vitrines do arquivo all.js.

##### vitrines/home

Mostra as vitrines selecionadas no arquivo all.js id 2 e id 3.

##### vitrines/destinos

Mostra o agrupamento de todas as vitrines, e exites uma barra de pesquisa que aplica filtros nas vitrines.

##### vritines/destinos/?limit=`<numero>`

Aplica um filtro que limita o numero de resultados.

##### vritines/destinos/?state=`<estado>`

Aplica um filtro que retorna apenas os resultados do estado escolhido resultados.

##### vritines/destinos/?text=`<texto>`

Aplica um filtro que faz retornar itens que contenham nome, pais, estado, cidade ou categoria semelhante ao texto inserido.

##### vitrines/sobre

Exibirá as informações de um item.

## Funcionalidades

##### Popular Banco de Dados

Convertir o arquivo all.js para all.json manualmente, por ser mais facil. Depois populei um banco de dados com o arquivo all.json da maneira mais fiel que consegui.

##### Concertar Imagens

As urls de imagens passadas foram quebradas, o arquivo concerta_images.py substitui por urls funcionais que foram mineradas do site https://viajarfazbem.com
