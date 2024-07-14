#include <iostream>
#include <string>

// O que era pra ser um sistema de estoque em C++ continua operável, porém não adaptado ainda.
// A opção (worm no sistema de estoque) se dá devido a uma brincadeira que eu fiz na época, devido a esse tipo de ataque comumente fazer múltiplas réplicas de si em uma rede.
// Essa minha brincadeira não causa definitivamente nenhum dano a qualquer máquina, os códigos podem ser lidos na linha 527 pra baixo.
// E o tamanho ABSURDO se dá devido a minha inexperiência na época.
// Feito por: Kevin Ricardo - 2022

using namespace std;

void opcao1() {
  double preco[20] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, inputPreco;
  int id[20] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, inputId, number, quantidade, intId;
  string produto[20] = {"-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",}, inputProduto, inputExclusao, confirmacao, troca, strProduto;
  char charOpcao;

do {

cout << "\n" << "\n";

cout << " Pressione \"a\" para adicionar produtos \n";
cout << " Pressione \"t\" para ir a tabela " << "\n";
cout << " Pressione \"e\" para excluir algum dado da tabela " << "\n";
cout << " Pressione \"u\" para atualizar algum dado da tabela " << "\n";
cout << " Ou senao aperte \"z\" para fechar o programa " << "\n";


cin >> charOpcao;
charOpcao = tolower(charOpcao);

if (charOpcao == 'a') {

cout << " Quantos produtos deseja adicionar? " << "\n";
cin >> quantidade;


while (quantidade > 20) {

    cout << " Quantidade invalida devera ser informado um valor entre: (1-20): ";
    cin >> quantidade;

}


quantidade = --quantidade;

cout << "\n";


  for (int i = 0; i <= quantidade; i++ ) {
        if (produto[i] == "-") {

            cout << " Informe o produto que deseja adicionar: ";
            cin >> produto[i];
            cout << "\n";

        } else {
          quantidade++;
        }

continue;


    cout << produto[0] << ", " << produto[1] << ", " << produto[2] << ", " << produto[3] << ", " << produto[4] << ", " << produto[5]
    << ", " << produto[6] << ", " << produto[7] << ", " << produto[8] << ", " << produto[9] << ", " << produto[10] << ", " << produto[11]
    << ", " << produto[12] << ", " << produto[13] << ", " << produto[14] << ", " << produto[15] << ", " << produto[16] << ", " << produto[17]
    << ", " << produto[18] << ", " << produto[19] << "\n \n"; // mostra todos os produtos j  cadastrados
break;
}



for (int i = 0; i <= quantidade; i++) {
    if (preco[i] == 0) {

        cout << "\n" << " Informe o preco do produto " << "(" << produto[i] << ")" << "\n";
        cin >> preco[i];

    }

    cout << preco[0] << ", " << preco[1] << ", " << preco[2] << ", " << preco[3] << ", " << preco[4] << ", " << preco[5] <<
    ", " << preco[6] << ", " << preco[7] << ", " << preco[8] << ", " << preco[9] << ", " << preco[10] << ", " << preco[11]
    << ", " << preco[12] << ", " << preco[13] << ", " << preco[14] << ", " << preco[15] << ", " << preco[16] << ", " << preco[17]
    << ", " << preco[18] << ", " << preco[19] << "\n \n"; // mostra todos os pre os cadastrados

   continue;  // continua o loop ate completar a condi  o do comando for

    break;

}

for ( int i = 0; i <= 19; i++) {
   if (produto[i] == "-" ) {

    id[i] = 0;
   } else {
     id[i] = 1;
     id[i] += i;
   }
    continue; // auto-incremento da id dos produtos cadastrados (utiliza  o breve)

    break;

}


 for (int i = 0; i <= 19; i++) {

    cout << " Id: " << id[i] << " ";
    cout << " Produto: " << produto[i] << " ";
    cout << " Preco: " << preco[i] << " " << "\n";

    continue; // mostra os id s, produtos e pre os cadastrados (utilizar para consultar em breve)

break;
}

}

cout << "\n\n";

system("cls"); // limpar a tela

// tabela mostrando o nome dos produtos para consulta de nome e pre o
cout << "tabela: " << '\n';
cout << "_______________________________________________________" <<
'\n' << "1 : " << produto[0] << "\t\t\t\t\t\t |" <<
'\n' << "2 : " << produto[1] << "\t\t\t\t\t\t |" <<
'\n' << "3 : " << produto[2] << "\t\t\t\t\t\t |" <<
'\n' << "4 : " << produto[3] << "\t\t\t\t\t\t |" <<
'\n' << "5 : " << produto[4] << "\t\t\t\t\t\t |" <<
'\n' << "6 : " << produto[5] << "\t\t\t\t\t\t |" <<
'\n' << "7 : " << produto[6] << "\t\t\t\t\t\t |" <<
'\n' << "8 : " << produto[7] << "\t\t\t\t\t\t |" <<
'\n' << "9 : " << produto[8] << "\t\t\t\t\t\t |" <<
'\n' << "10 : " << produto[9] << "\t\t\t\t\t\t |" <<
'\n' << "11 : " << produto[10] << "\t\t\t\t\t\t |" <<
'\n' << "12 : " << produto[11] << "\t\t\t\t\t\t |" <<
'\n' << "13 : " << produto[12] << "\t\t\t\t\t\t |" <<
'\n' << "14 : " << produto[13] << "\t\t\t\t\t\t |" <<
'\n' << "15 : " << produto[14] << "\t\t\t\t\t\t |" <<
'\n' << "16 : " << produto[15] << "\t\t\t\t\t\t |" <<
'\n' << "17 : " << produto[16] << "\t\t\t\t\t\t |" <<
'\n' << "18 : " << produto[17] << "\t\t\t\t\t\t |" <<
'\n' << "19 : " << produto[18] << "\t\t\t\t\t\t |" <<
'\n' << "20 : " << produto[19] << "\t\t\t\t\t\t |" <<
'\n' << "_______________________________________________________"; // tabela que mostra a ordem e os produtos j  cadastrados


if (charOpcao == 't') {

do { //comando para executar os numeros pelos menos 1 (uma) vez se est  dentro dos requisitos do while
    number = 0;
    cout << "\n \n" << " Escolha um numero na tabela " << "\n";
    cout << " Senao coloque \"0\" para voltar " << "\n\n";
    cin >> number;
    if (number == 000) {
        number = number;
    }

 for (int i = 19; i >=0; i--) {
    if ( number == 20) {
      cout << "__________________" << "\n";
      cout << "id: " << id[19] << "\n";
      cout << "produto: " << produto[19] << "\n";
      cout << "valor: " << preco[19] << "\n";
      cout << "__________________" << "\n";
    } else {
    if ( number == 19) {
      cout << "__________________" << "\n";
      cout << "id: " << id[18] << "\n";
      cout << "produto: " << produto[18] << "\n";
      cout << "valor: " << preco[18] << "\n";
      cout << "__________________" << "\n";
    } else {
    if ( number == 18) {
      cout << "__________________" << "\n";
      cout << "id: " << id[17] << "\n";
      cout << "produto: " << produto[17] << "\n";
      cout << "valor: " << preco[17] << "\n";
      cout << "__________________" << "\n";
    } else {
    if (number == 17) {
      cout << "__________________" << "\n";
      cout << "id: " << id[16] << "\n";
      cout << "produto: " << produto[16] << "\n";
      cout << "valor: " << preco[16] << "\n";
      cout << "__________________" << "\n";
    } else {
    if ( number == 16) {
      cout << "__________________" << "\n";
      cout << "id: " << id[15] << "\n";
      cout << "produto: " << produto[15] << "\n";
      cout << "valor: " << preco[15] << "\n";
      cout << "__________________" << "\n";
    } else {
    if (number == 15) {
      cout << "__________________" << "\n";
      cout << "id: " << id[14] << "\n";
      cout << "produto: " << produto[14] << "\n";
      cout << "valor: " << preco[14] << "\n";
      cout << "__________________" << "\n";

    } else {
    if (number == 14) {
      cout << "__________________" << "\n";
      cout << "id: " << id[13] << "\n";
      cout << "produto: " << produto[13] << "\n";
      cout << "valor: " << preco[13] << "\n";
      cout << "__________________" << "\n";

    } else {
    if (number == 13) {
      cout << "__________________" << "\n";
      cout << "id: " << id[12] << "\n";
      cout << "produto: " << produto[12] << "\n";
      cout << "valor: " << preco[12] << "\n";
      cout << "__________________" << "\n";

    } else {
    if (number == 12) {
      cout << "__________________" << "\n";
      cout << "id: " << id[11] << "\n";
      cout << "produto: " << produto[11] << "\n";
      cout << "valor: " << preco[11] << "\n";
      cout << "__________________" << "\n";

    } else {
     if (number == 11) {
      cout << "__________________" << "\n";
      cout << "id: " << id[10] << "\n";
      cout << "produto: " << produto[10] << "\n";
      cout << "valor: " << preco[10] << "\n";
      cout << "__________________" << "\n";

    } else {
    if (number == 10) {
      cout << "__________________" << "\n";
      cout << "id: " << id[9] << "\n";
      cout << "produto: " << produto[9] << "\n";
      cout << "valor: " << preco[9] << "\n";
      cout << "__________________" << "\n";

    } else {
    if (number == 9) {
      cout << "__________________" << "\n";
      cout << "id: " << id[8] << "\n";
      cout << "produto: " << produto[8] << "\n";
      cout << "valor: " << preco[8] << "\n";
      cout << "__________________" << "\n";

    } else {
    if (number == 8) {
      cout << "__________________" << "\n";
      cout << "id: " << id[7] << "\n";
      cout << "produto: " << produto[7] << "\n";
      cout << "valor: " << preco[7] << "\n";
      cout << "__________________" << "\n";

    } else {
    if (number == 7) {
      cout << "__________________" << "\n";
      cout << "id: " << id[6] << "\n";
      cout << "produto: " << produto[6] << "\n";
      cout << "valor: " << preco[6] << "\n";
      cout << "__________________" << "\n";

    } else {
    if (number == 6) {
      cout << "__________________" << "\n";
      cout << "id: " << id[5] << "\n";
      cout << "produto: " << produto[5] << "\n";
      cout << "valor: " << preco[5] << "\n";
      cout << "__________________" << "\n";

    } else {
    if (number == 5) {
      cout << "__________________" << "\n";
      cout << "id: " << id[4] << "\n";
      cout << "produto: " << produto[4] << "\n";
      cout << "valor: " << preco[4] << "\n";
      cout << "__________________" << "\n";

    } else {
    if (number == 4) {
      cout << "__________________" << "\n";
      cout << "id: " << id[3] << "\n";
      cout << "produto: " << produto[3] << "\n";
      cout << "valor: " << preco[3] << "\n";
      cout << "__________________" << "\n";

    } else {
    if (number == 3) {
      cout << "__________________" << "\n";
      cout << "id: " << id[2] << "\n";
      cout << "produto: " << produto[2] << "\n";
      cout << "valor: " << preco[2] << "\n";
      cout << "__________________" << "\n";

    } else {
    if (number == 2) {
      cout << "__________________" << "\n";
      cout << "id: " << id[1] << "\n";
      cout << "produto: " << produto[1] << "\n";
      cout << "valor: " << preco[1] << "\n";
      cout << "__________________" << "\n";

    } else {
    if (number == 1) {
      cout << "__________________" << "\n";
      cout << "id: " << id[0] << "\n";
      cout << "produto: " << produto[0] << "\n";
      cout << "valor: " << preco[0] << "\n";
      cout << "__________________" << "\n";

    }
    }
    }
    }
    }
    }
    }
    }
    }
    }
    }
    }
    }
    }
    }
    }
    }
    }
    }
    }
    break;
 }


 } while (number == 1 || number == 2 || number == 3 || number == 4 || number == 5 || number == 6 || number == 7 || number == 8 || number == 9 || number == 10 || number == 11 || number == 12 || number == 13 || number == 14 || number == 15 || number == 16 || number == 17 || number == 18 || number == 19 || number == 20 );

system("cls"); // limpar a tela

} else {
    if (charOpcao == 'e') {


        cout << "\n\t\t\t" << "ATENCAO!!" << "\n";
        cout << " [ Produtos com nome repetidos serao apagados tambem, use a id do produto se for necessario ] " << "\n";
        cout << "\n" << " Deseja informar o PRODUTO ou ID? " << "\n";
        cout << " Caso contario coloque \"0\" para voltar" << "\n";

        cin >> troca;


        if (troca == "produto" || troca == "Produto" || troca == "PRODUTO") {

                cout << " Informe o nome do produto: ";
                cin >> inputExclusao;


                for (int i = 0; i <= 19; i++) {

                    if ( produto[i] == inputExclusao) {

                        produto[i] = "-";
                        preco[i] = 0;
                        system("cls");
                        cout << "\n" << " Produto excluido com sucesso! " << "\n " << " Id do produto: " << id[i] << "\n";

                    }

                }


        } else {
        if (troca == "id" || troca == "Id" || troca == "ID") {

            cout << " Informe a Id do produto: ";
            cin >> intId;
            troca = intId;

            for ( int i = 0; i <= intId; i++) {

          if ( id[i] == intId ) {

           produto[i] = "-";
           preco[i] = 0;
           system("cls");
           cout << "\n" <<"produto excluido com sucesso!" << "\n " << " id do produto: " << id[i] << "\n";

          }

           continue;
           break;

          } // fim do comando for



        } else {

            system("cls");
            cout << "nenhum dado alterado " << "\n";

        }

        }


       } else {
            if (charOpcao == 'u') {

                inputId = 0;
                cout << "\n \n" << " Atualizacao do produto e feita pelo numero de identificacao dele na tabela (ao lado do nome) " << "\n";
                cout << " Coloque a id do produto logo abaixo " << "\n";
                cout << " Caso contrario coloque \"0\" " << "\n";
                cin >> inputId;


                if (inputId > 0) {


                for (int i = 0; i <= 19; i++) {
                    if (id[i] == inputId) {

                        cout << "o produto a ser atualizado sera este? " << "\n";
                        cout << "id: " << id[i] << "/" << produto[i] << "/" << preco[i] << "\n";
                        cout << "(sim ou nao) " << "\n";
                        cin >> confirmacao;

                        if ( confirmacao == "sim" || confirmacao == "Sim" || confirmacao == "SIM") {

                            cout << "Qual sera o produto e o valor dele? " << "\n";
                            cout << "produto novo: ";
                            cin >> produto[i];
                            cout << "valor novo: ";
                            cin >> preco[i];

                            continue;

                        } else {
                        if (confirmacao == "nao" || confirmacao == "n o") {


                                confirmacao = "-";
                                cout << "deseja escolher outra id? " << " (sim ou nao) " << "\n";
                                cin >> confirmacao;

                                if (confirmacao == "sim") { // devo apagar a parte de cima do loop e manter somente o loop para que seja feito os testes

                                        confirmacao = "nao";

                                  do {


                                    inputId = 0;
                                    cout << " Coloque a id do produto: ";
                                    cin >> inputId;



                                    for (int i = 0; i <= 19; i++) {

                    if (inputId == id[i]) {

                        cout << "o produto a ser atualizado sera este? " << "\n";
                        cout << "id: " << id[i] << "/" << produto[i] << "/" << preco[i] << "\n" ;
                        cout << "(sim ou nao) " << "\n";
                        cin >> confirmacao;

                         if ( confirmacao == "sim" || confirmacao == "Sim" || confirmacao == "SIM") {

                            cout << "Qual sera o produto e o valor dele? " << "\n";
                            cout << "produto novo: ";
                            cin >> produto[i];
                            cout << "valor novo: ";
                            cin >> preco[i];


                        }


                    }

                continue;

            break;
                  } // fim do comando for




                  break;

                  } while (confirmacao == "nao" || confirmacao == "n o") ; // fim do comando while

                            }



            }

            }


        }



    } // fim do comando for que ser apagado para testes


                }

    }

       } // fim do else (u) (meu codigo precisa ser dentro dele) [para lembrar] ok ;)


    } // fim do else (e) (meu codigo precisa ser dentro dele) [para lembrar] ok ;)

} while (charOpcao != 'z');

}

// WORM
void wormSystem1() {
int var1[100] = {0,0,0,0,0,0,0,0,0,0},
var2 = 0,
var = 0;
string intOpcao = "z";

do {

while (var1[99] == 0) {

for (int i = 0; i <= 99; i++) {
        if (var1[i] == 0){


        cout << var1[i]++ << "\n";
        var1[i]++;

        } else {
        if (var1[99] == 1);
        }
    }

}
   cout << "array de var[99] e igual: " << var1[99] << "\n";

   exit(1);

   if( var1[0] >= 1){

    intOpcao = "z";

    if (intOpcao == "z") {

       do {

    switch (var2 == 0) {

        case 0:

            cout << "hoje   domingo";

            continue;
    }


   } while (intOpcao == "z");

   }

   }


   break;

}while (intOpcao == "w");

}


int main() {
int opcaoVoid;

cout << " Seja bem vindo, qual sistema deseja acessar? " << "\n \n";
cout << " Digite 1 para sistema de estoque " << "\n";
cout << " Digite 2 para worm no sistema de estoque " << "\n";

cin >> opcaoVoid;

if (opcaoVoid == 1) {
    opcao1();

} else {
if (opcaoVoid == 2 ) {
    wormSystem1();

}

}

exit(1);
cout << "\n \n" << " EMAIL DE CONTATO: KEVINNIZA16@GMAIL.COM " << "\n \n";


return 0; }
