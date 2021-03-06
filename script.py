from app.models import Desafio, Regra_Casa 

#exec(open('script.py').read())

def validacao_frase_desafio(frase_desafio):
    try:
        desafio = Desafio.objects.get(frase=frase_desafio)
        if desafio: 
            return False
        else:
            return True
    except:
        return True
        
list_desafios = {
    "facil": [
        "Vá até o banheiro e tire sua calcinha ou cueca, depois deixe-o na sua cabeça pelo resto do jogo.",
        "Uma pessoa irá jogar algo no vaso sanitário e depois você tem que pegar de volta com as próprias mãos.",
        "Tente fazer malabarismos com 3 objetos que o grupo escolher.",
        "Tente beber um copo de água (ou cerveja, caso tenha) usando os seus pés.",
        "Publique uma foto sua embaraçosa no seu Instagram ou Facebook.",
        "Molhe o rosto e passe farinha nele.",
        "Ligue para um amigo e diga que está grávida ou que vai ser pai.",
        "Ligue para uma lanchonete ou pizzaria e tente desabafar com o atendente, dizendo que seu namorada (o) terminou contigo.",
        "Ligue para sua mãe chorando dizendo que quer sua chupeta.",
        "Ligue para o quinto contato no seu telefone e cante um trecho de uma música que o grupo escolher.",
        "Invente um rap sobre sua situação amorosa atual.",
        "Finja ser um gato e se esfregue em todas as pessoas do grupo.",
        "Finja ser o animal de estimação da pessoa à sua esquerda.",
        "Finja que você é um peixe se debatendo fora d’água.",
        "Finja que você está parindo uma criança.",
        "Fale com um sotaque diferente pelo resto do jogo.",
        "Faça um chá com alguma coisa estranha (tipo uma meia) e depois beba.",
        "Faça uma serenata para alguém do grupo.",
        "Faça uma mímica descrevendo seu filme favorito para que o grupo adivinhe.",
        "Faça uma maquiagem em si mesmo usando itens e condimentos da cozinha.",
        "Faça uma apresentação de dança do ventre.",
        "Faça o quadradinho de oito (ou tente)",
        "Faça lip sync (dublagem) de alguma música que o grupo escolher.",
        "Deixe que alguém te dê um tapa na cara.",
        "Deixe que alguém do grupo envie uma foto que ele escolher para algum contato.",
        "Deixe o grupo te colocar em uma posição embaraçosa e tire uma foto.",
        "Deixe alguém depilar uma parte do seu corpo.",
        "Dance alguma música que o grupo escolher.",
        "Coma uma colher cheia de pimenta ou molho picante.",
        "Coloque um cubo de gelo nas suas calças.",
        "Cheire as axilas da pessoa a sua direita.",
        "Cheire a axila da pessoa que estiver à sua direita.",
        "Cante uma música de funk como se fosse uma ópera.",
        "Beba um shot de alguma bebida alcoólica e depois gire por 30 segundos (somente para maiores de idade).",
        "Beba alguma mistura que o grupo irá fazer.",
        "Arraste sua bunda no tapete como se fosse um cachorro.",
        "A pessoa terá que lamber o rosto de todas as pessoas do mesmo gênero que ela do círculo.",
        "Alguém do grupo irá escrever algo embaraçoso no seu corpo com uma caneta permanente.",
        "Se enrole em papel higiênico até ficar parecido com uma múmia.",
        "Saia de casa ou vá na sua varanda e grite bem alto 'eu ainda amo meu ex'.",
        "Ligue para um restaurante e tente manter o atendente em linha por cinco minutos imitando um gringo falando português.",
        "Ligar para o ex ou para ex e dizer 'Oi, sumido(a)'.",
        "Jogar o resto do jogo com as mãos para trás, sem poder soltar ou pegar algo.",
        "Passar um trote para algum amigo que não está jogando.",
        "Mandar uma imagem aleatória por mensagem para o pai ou mãe e esperar a resposta.",
        "Mostrar para o grupo o que falou nas 3 últimas conversas do WhatsApp.",
        "Mostrar para o grupo as 5 últimas fotos da galeria do celular.",
        "Dar uma volta correndo na quadra.",
        "Pedir ou comprar alguma comida para o grupo.",
        "Andar pela casa\apartamento pulando num pé só.",
        "Dizer a alguma pessoa do grupo qual o maior defeito dela.",
        "Dizer ao grupo quem foi a pessoa que você já beijou e foi o melhor beijo da sua vida.",
        "Ficar de mãos dadas com a pessoa que você tem menos intimidade da roda, durante toda a jogada.",
        "Dançar um ritmo musical que não gosta, na frente de todo o grupo.",
        "Deixar que todo mundo diga coisas engraçadas e vergonhosas que já passaram juntos.",
        "Levar uma ovada no cabelo.",
        "Colocar chantili no rosto.",
        "Pôr o rosto na farinha de trigo.",
        "Deixar que cada participante faça um pouco de maquiagem no seu rosto.",
        "Quebrar o ovo com a boca.",
        "Pintar os dentes e o meio da sobrancelha com lápis de olho preto.",
        "Fazer um desenho no rosto com tinta guache.",
        "Deixar que uma pessoa do grupo lamba o seu rosto.",
        "Escrever o nome de todos os participantes no braço, com canetinha ou caneta.",
        "Tomar 200ml de água morna com limão.",
        "Chupar o limão sem fazer cara feia.",
        "Falar “três tigres tristes” por um minuto, o mais rápido possível, sem errar.",
        "Cantar uma música até o final sem errar.",
        "Dizer o nome de todos os participantes do grupo, mas ao contrário.",
        "Ser vendado, passar a mão no rosto de cada participante e dizer quem é sem errar.",
        "Colocar um fone com música alta, enquanto as outras pessoas no grupo fazem três perguntas que devem ser respondidas com “sim” ou “não”.",
        "Comer um tomate inteiro com açúcar.",
        "Comentar a primeira foto de uma pessoa que você segue no Instagram (não vale pessoas famosas).",
        "Contar 2 coisas engraçadas que aconteceram na sua vida e que ninguém do grupo sabe.",
        "Contar com qual pessoa que você já ficou e ninguém sabe.",
        "Fazer o máximo de flexões que conseguir em 1 minuto.",
        "Passar o resto do jogo com uma panela na cabeça.",
        "Enviar mensagem para 5 contatos no WhatsApp que você não conversa normalmente.",
        "Tomar uma colher de azeite de oliva.",
        "Dizer qual a maior mentira que você já contou na sua vida.",
        "Enviar um meme para alguém mais idoso da sua família e esperar a resposta.",
        "Ficar o resto do jogo com dois copos cheios de água nas mãos sem soltar.",
        "Desenhar uma pessoa do grupo num papel.",
        "Andar de costas por 2 minutos sem esbarrar em nada.",
        "Dar ou transferir R$5,00 para alguém do grupo.",
        "Gritar “Eu te amo” na rua.",
        "Ligar para alguém que conhece e começar a pedir desculpa sem dizer o motivo.",
        "Ir à rua e apertar a mão de um desconhecido.",
        "Falar em espanhol ou inglês com alguém na rua, que você não conhece.",
        "Falar eu te amo para uma pessoa aleatória.",
        "Cantar uma música bem alto em um lugar público.",
        "Cantar “parabéns para você” bem alto num lugar público.",
        "Imitar o jeito de falar e andar de alguém do grupo.",
        "Dançar um brega-funk.",
        "Correr pela casa ou pela rua com um ovo na colher, sem deixar cair.",
        "Beber um copo d’água sem usar as mãos ou canudo.",
        "Equilibrar um garfo na testa por 3 minutos.",
        "Publicar a sua primeira foto da galeria do celular, no Instagram.",
        "Ligar para a última pessoa que mandou mensagem",
        "Vá ao banheiro, tire uma peça intima e passe o jogo inteiro com ela nas mãos.",
        "Fingir ser um dinossauro.",
        "Ligar para um amigo ou amiga e dizer que será pai ou mãe.",
        "Conte, em terceira pessoa, uma história sobre a sua vida amorosa atual.",
        "Segurar um gelo nas mãos até derreter.",
        "Tentar adivinhar a cor da calcinha ou cueca da pessoa a sua direita.",
        "Beijar o queixo de todas as pessoas da roda.",
        "Deixar que uma pessoa do grupo escreva ou desenhe algo nos seus braços.",
        "Enrolar a cabeça com papel higiênico e fica assim até o final do jogo.",
        "Segurar três limões na mão até o jogo acabar.",
        "Imitar a voz da mulher do Google Tradutor.",
        "Beber alguma mistura feita pelo grupo.",
        "Comer uma colher de sopa de três temperos escolhidos pelo grupo.",
        "Fazer agachamentos por 1 minuto.",
        "Mandar a mensagem “ainda amo o meu ex” (ou a minha ex) para algum amigo.",
        "Publicar uma foto embaraçosa nos stories.",
        "Fazer mímica de um filme ou série até que alguém do grupo adivinhe.",
        "Falar com o sotaque de outro estado até o final do jogo.",
        "Ficar com a mão na cabeça da pessoa a sua esquerda pelo resto do jogo.",
        "Fazer uma videochamada com um amigo e finja que a conexão está falhando.",
        "Escrever uma mensagem falando mal de um amigo e enviar para ele mesmo.",
        "Andar de lado, como caranguejo, por toda a casa ou apartamento.",
        "Brinque com as condições climáticas e do lugar. Por exemplo, se está frio, desafie a pessoa a dar uma volta pela casa sem casaco. Se está calor, a pular na piscina de roupa.",
        "Ser a pessoa que serve as bebidas até o final dessa rodada.",
        "Virar um shot de alguma bebida.",
        "Dance o funk do momento equilibrando um copo na cabeça.",
        "Parar na frente de uma janela na rua e começar a cantar uma serenata.",
        "Dê um beijo no pé da pessoa do seu lado direito.",
        "Ficar sem olhar o celular até o final da brincadeira.",
        "Trocar o status de relacionamento no Facebook.",
        "Postar uma foto feia nas redes sociais.",
        "Dance uma música de forró com alguém da roda.",
        "Fazer um elogio a um desconhecido na festa ou na rua.",
        "Escolher uma música para cantar até o final sem errar.",
        "Encenar um trecho de filme para todos.",
        "Rebolar em um bambolê imaginário.",
        "Escolha alguém para publicar uma mensagem qualquer em seu Facebook.",
        "Ficar sem usar a palavra 'não' até o final da rodada ou brincadeira.",
        "Lamber o cotovelo.",
        "Encostar a língua no nariz.",
        "Colocar o pé atrás da cabeça.",
        "Escolher alguém da roda para dançar valsa e dançarem.",
        "Fazer uma imitação de algum famoso ou de alguém que está na roda.",
        "Passar uma rodada brincando com os olhos vendados.",
        "Ligar para alguém que por algum motivo a pessoa não conversa há muito tempo.",
        "Passar uma rodada falando com algum sotaque ou em outro idioma.",
        "Mastigar um alho cru.",
        "Crie uma música de rap usando nome de todos que fazem parte da brincadeira.",
        "Jogue capoeira com alguém da roda.",
        "Comer uma colher com canela.",
        "Fique com 1 cubo de gelo no bolso até o final da brincadeira.",
        "Engolir um gelo em menos de 1 minuto sem voltá-lo ao copo.",
        "Cantar uma música sem olhar a letra.",
        "Inventar uma poesia que rime com alguma palavra (escolher uma palavra bizarra).",
        "Simular um pedido de casamento.",
        "Improvisar um número de musical com a situação da brincadeira.",
        "Tomar 1 litro de água no menor tempo possível.",
        "Fazer uma parada de mãos.",
        "Dance frevo.",
        "Tirar uma peça de roupa (casaco, sapatos, brincos...)",
        "Fazer o máximo de flexões que você conseguir em 1 minuto.",
        "Desligar o celular até o final do jogo.",
        "Falar na língua do 'pê' até o final da rodada.",
        "Abrir uma garrafa de cerveja sem abridor.",
        "Mude a sua foto de perfil no Facebook com a sua pior foto.",
        "Passar a próxima rodada com os olhos vendados.",
        "Pronunciar 'farofa' com 1 colher e farofa na boca.",
        "Fazer uma pose de yoga.",
        "Improvisar uma coreografia de balé.",
        "Toma água de uma tigela como se fosse um cachorro.",
        "Imitar um gato se limpando.",
        "Revelar a última mensagem que você mandou no WhatsApp.",
        "Receber cócegas de alguém por 1 minuto.",
        "Lavar os pés de alguém da roda.",
        "Envie para algum contatinho alguma das melhores cantadas do WhatsApp.",
        "Dançar 'na boquinha da garrafa' (ou alguma dança do momento).",
        "Pedir para fazer um discurso no meio da festa (sem que as pessoas saibam que se trata de uma brincadeira).",
        "Fingir que está na balada e mostrar como você faria para chegar em alguém.",
        "Chupar um limão como se fosse uma laranja.",
        "Faça algumas das brincadeiras do artigo sobre os melhores jogos de bebidas.",
        "Mostrar as suas últimas mensagens do WhatsApp aqui na roda.",
        "Mostre a última foto que você tirou de você mesmo no celular.",
        "Fazer uma dança sensual usando só uma perna.",
        "Publique uma enquete no seu Instagram perguntando se 'é normal ter verrugas na bunda?' (ou alguma das ideias do artigo sobre as melhores perguntas para enquetes no Instagram).",
        "Tome o gole de algo e faça uma análise detalhada como se fosse um especialista em vinhos.",
        "Mostre para a galera qual foi o último vídeo que você assistiu no YouTube.",
        "Dançar arrocha com alguém da roda ao som de música clássica.",
        "Dê uma cambalhota.",
        "Colocar o máximo de uvas na boca que você conseguir.",
        "Participar de uma competição de natação imaginária no chão.",
        "Dê 10 beijinhos no chão, com muito amor.",
        "Corte uma cebola e simule uma cena de novela triste.",
        "Penteie o cabelo de alguém da roda.",
        "Passe as próximas 2 rodadas imitando um animal.",
        "Cante o hino do seu time de futebol rival.",
        "Arrotar o abecedário.",
        "Faça uma performance ao som de uma música do Michael Jackson (Rusbé).",
        "Dar uma aula de axé anos 90.",
        "Sair na rua e gritar bem alto: 'eu não aguento mais essa coceira na minha bunda'.",
        "Dançar em cima da mesa.",
        "Use meias de alguém da roda como fossem as suas luvas.",
        "Assistir um vídeo engraçado na internet com a boca cheia de água.",
        "Curtir fotos antigas de uma pessoa que você não segue no Instagram.",
        "Postar uma enquete no Stories do Instagram pedindo dicas de como parar uma diarreia.",
        "Publicar um vídeo cantando.",
        "Virar um shot de bebida sem fazer careta.",
        "Faça um show de dança ao som do funk da moda.",
        "Faça uma performance digna de um show de rock.",
        "Passe a próxima rodada congelado, como se fosse uma estátua viva.",
        "Poste um stories no Instagram com uma enquete do tipo: 'é normal ter caroços azuis nas partes íntimas?'",
        "Mande uma mensagem para uma pessoa que você não conversa há mais de um ano.",
        "Mude o status de relacionamento no Facebook.",
        "Altere a sua foto de perfil no WhatsApp para a foto mais feia que você tem no seu celular.",
        "Faça o passinho do cocô, do Ticolé.",
        "Se aproxime de pessoas desconhecidas e comece a fazer a dança da chuva.",
        "Chegue para alguém desconhecido e comece a defender o político que você mais odeia.",
        "Publique uma selfie com o dedo no nariz.",
        "Passar o resto do jogo se comportando como um animal que o grupo escolheu.",
        "Tente voar.",
        "Cheirar as axilas de alguém da roda.",
        "Faça 50 abdominais como se fosse uma musa fitness enquanto o grupo conta.",
        "Uive como um lobo.",
        "Tomar um danoninho usando apenas a língua.",
        "Fazer uma lap dance (dança no colo) para alguém da roda.",
        "Dar uma aula de educação sexual de uma maneira muito sexy.",
        "Colocar um preservativo em uma banana ou pepino.",
        "Colocar um preservativo em uma fruta com a boca.",
        "Massagear alguém da roda.",
        "Faça uma massagem nas costas de alguém sem usar as mãos.",
        "Tirar o sutiã sem tirar a camiseta.",
        "Simule uma dança em pole dance.",
        "Desabotoar o sutiã de alguém usando só uma mão.",
        "Fingir um orgasmo.",
        "Tirar a camiseta de alguém usando a boca.",
        "Sussurrar uma frase sensual no ouvido de alguém.",
        "Beijar a orelha de alguém da roda.",
        "Fazer um discurso como se estivesse prestes à chegar a um orgasmo.",
        "Poste uma foto fazendo cara de sensual no seu stories do Instagram.",
        "Recitar um poema erótico.",
        "Uma rodada fazendo cafuné em alguém da roda.",
        "Explique onde está o clítoris.",
        "Faça uma selfie sensual.",
    ],
    
    "medio": [
        "imule o seu olhar mais sexy para alguém da roda.",
        "Tomar um shot no umbigo de alguém (body shot).",
        "Sussurre no ouvido de alguém as coisas que você costuma dizer na hora do sexo.",
        "Morder (de leve) o pescoço de alguém da roda.",
        "Com os olhos fechados, encoste a mão em alguém da roda e adivinhe qual é a parte do corpo.",
        "Passar a próxima rodada no colo de alguém.",
        "Chupar uma fruta como se fosse um órgão sexual.",
        "Simule sexo oral com uma fruta.",
        "Masturbar uma fruta com os dedos como se você estivesse falando com outra pessoa.",
        "Com o consentimento, beije alguém da roda.",
        "Simular um strip tease tirando uma peça de roupa.",
        "Faça uma simulação no ar da sua posição sexual favorita.",
        "Coloque um cubo de gelo na boca e dê um beijo no pescoço de alguém da roda.",
        "Mande uma mensagem de voz sexy para seu crush.",
        "Lamber alguma parte do corpo de outra pessoa.",
        "Passe creme em alguém.",
        "Feche os olhos, alguém da roda te dá um beijo, você precisa adivinhar quem é.",
        "Mande uma mensagem para o crush perguntando se ele quer jogar verdade ou desafio virtual.",
        "Envie um sticker sexy para seu crush.",
        "Publique 'hoje eu tô soltinh@' no seu Facebook'.",
    ],
    
    "dificil": [
        "Mande uma mensagem bem ousada para algum contato do seu celular 'acidentalmente'.",
        "Abaixe suas calças no meio da rua.",
        "Vá na varanda e mostre suas partes íntimas.",
        "Faça uma dança sensual para alguém do círculo.",
        "Tire uma fotografia íntima no banheiro e mostre para alguém do grupo por 5 segundos.",
        "Procure um 'filme picante' na internet e narre com detalhes para o grupo.",
        "Envie uma mensagem de texto extremamente ousada e suja que você possa imaginar para todos aqui do grupo.",
        "Tire uma peça de roupa a cada vez que você falar a palavra 'não' durante o jogo.",
        "Faça bodyshot em alguém do grupo (colocar bebida no corpo de alguém e depois beber).",
        "Finja que está tendo relações íntimas com alguém.",
        "Coloque uma música sexy e dance enquanto tira a roupa para o grupo.",
        "Deixe que alguém do grupo te faça uma marca no corpo usando a boca.",
        "Finja que você está atingindo o ápice do prazer durante uma relação.",
        "Mande uma fotografia semi-íntima para um contato do seu celular.",
        "Use sua boca para abrir as calças de alguém de sua escolha.",
        "Coma uma banana (ou enfie algo na boca) de forma muito insinuativa.",
        "Responda os stories de alguém dizendo que a pessoa te deixou excitada.",
        "Passe um cubo de gelo da sua boca para a boca da pessoa à sua esquerda.",
    ],
}

nivel_desafio = ['facil', 'medio', 'dificil']

for indice in nivel_desafio:
    print("\n\n---------------------------------------") 
    print("\niniciando cadastro - desafio {}\n".format(indice))
    for frase in list_desafios[indice]:
        if(validacao_frase_desafio(frase)):
            print(frase)
            desafio = Desafio()
            desafio.nivel_desafios = "{}".format(indice[0])
            desafio.frase = frase
            desafio.save()
        else:
            print("\nERRO! A Opção: {}, já está cadastrada no banco de dados!".format(frase))
            