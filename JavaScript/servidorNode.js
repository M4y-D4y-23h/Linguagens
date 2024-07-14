const express = require('express')
const app = express()
const ejs = require('ejs')
const path = require('path')
const views = path.join(__dirname, 'views')

// Código JavaScript criado para uma atividade escolar que cria um servidor node e envia alguns dados às páginas HTML e faz requisições.
// Feito por: Kevin Ricardo

app.set('views', views)
app.engine('html', ejs.renderFile)
app.use(express.static(path.join(__dirname, 'public')))

function renderpag(caminho, site, dados) {
    app.get(caminho,(req, res)=>{
        ejs.renderFile(path.join(views, site), {dados}, (err, html)=>{
            err ? console.log('erro ao renderizar a view') : res.send(html)
        })
    })
}

renderpag('/', 'index.html', {
    titulo:'Bem vindo ao \'ETEC Gamejam\'!',
});
renderpag('/home', 'home.html', {
    titulo:'Home!',
    conteudo: 'Descubra sobre tudo que site tem a oferecer.'
});
renderpag('/cadastro_alunos', 'cadastro_alunos.html', {
    titulo:'Cadastro de alunos',
    conteudo:'Discente, cadastre-se aqui!',
    usuario:'...',
    senha:'*****'
});
renderpag('/cadastro_professores', 'cadastro_professores.html', {
    titulo:'Cadastro de professores',
    conteudo:'Docente, cadastre-se aqui!',
    usuario:'...',
    senha:'*****'
});
renderpag('/login', 'login.html', {
    titulo:'Login',
    conteudo:'Entre em sua conta',
    usuario:'...',
    senha:'*****'
});

app.listen(3000,()=>{console.log('Servidor iniciado na porta 3000.')})
