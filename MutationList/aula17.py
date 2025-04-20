"""
 Usando uma lista como armazenamento conforme especificação abaixo, exiba um menu de opções
que fique em execução conƟnuamente, até que o usuário escolha a opção de finalização. Não deve ser
permiƟda a inclusão de nome de contato repeƟdo. Cada contato pode ter quantos telefones desejar.
Estrutura de dados:
Agenda=['Contato 1', ['99876-5645','98798-3244'], 'Contato 2',['99786-5531'], ..., 'Contato N',['99654-
1123', '99874-5532 ', '99874-8879’ ]]
1- Incluir contato e telefone (pelo menos um telefone)
2- Alterar um telefone de um contato (mostre as opções e o usuário digita qual será alterado)
3- Excluir um telefone de um contato (mostre as opções e o usuário digita qual será excluído
4- Consultar os telefones de um contato (forma formatada)
5- Listar todos os contatos e seus respecƟvos telefones (forma formatada)
6 – FIM
Digite a opção desejada:
"""

agenda = []

while agenda == [] or userInputChoice != 'FIM':
    agenda = ['Contato 1', ['99876-5645','98798-3244'], 'Contato 2',['99786-5531']]
    print('1- Incluir contato e telefone (pelo menos um telefone)') # foi
    print('2- Alterar um telefone de um contato (mostre as opções e o usuário digita qual será alterado)')
    print('3- Excluir um telefone de um contato (mostre as opções e o usuário digita qual será excluído')
    print('4- Consultar os telefones de um contato (forma formatada)')
    print('5- Listar todos os contatos e seus respecƟvos telefones (forma formatada)') # foi
    print('6- FIM')

    print()
    userInputChoice = input('Digite a opção desejada:')
    print()


    if userInputChoice == '1':
        userInputNameContact = input('Informe o nome do contato: ')
        apendUser = True
        for i in agenda:
            if i == userInputNameContact:
                apendUser = False
        
        if apendUser:
            contacts = []
            
            userInputNumberContact = input('Informe o contato ou "s" para sair: ')

            while userInputNumberContact != 's':
                contacts.append(userInputNumberContact)
                userInputNumberContact = input('Informe o contato ou "s" para sair: ')

            if contacts:
               agenda.append(userInputNameContact)
               agenda.append(contacts)

            else:
                print('informe pelo menos um contato') 
        else:
            print('Contato já cadastrado') 
        
        print()
           

    elif userInputChoice == '2':
        
        printNameContact = True
        for contactsName in agenda:
            if printNameContact:
                print(f'Contato: {contactsName}')
                printNameContact = False
            else:
                cont = 1
                for contactsNumber in contactsName:
                    print(f'\t{cont}° número: {contactsNumber}')
                    printNameContact = True
                    cont += 1
        print()
        
        userInputChoiceContactName = input('Informe o nome do contato: ')
        userInputChoiceNumberContact = int(input('Informe o numero da opção do telefone: '))
        userInputNewNumberContact = input('Informe o novo telefone do contato: ')

        lastContactsName = ''
        countContatcts = 0
        for contactsName in agenda:

            if lastContactsName == userInputChoiceContactName:
                countContatctsNumber = 1
                for contactsNumber in contactsName:
              
                    if countContatctsNumber == userInputChoiceNumberContact:
                        agenda[countContatcts][countContatctsNumber - 1] = userInputNewNumberContact
        
                    countContatctsNumber += 1

            countContatcts += 1
            lastContactsName = contactsName

    elif userInputChoice == '3':
        printNameContact = True
        for contactsName in agenda:
            if printNameContact:
                print(f'Contato: {contactsName}')
                printNameContact = False
            else:
                cont = 1
                for contactsNumber in contactsName:
                    print(f'\t{cont}° número: {contactsNumber}')
                    printNameContact = True
                    cont += 1
        print()
        
        userInputChoiceContactName = input('Informe o nome do contato: ')
        userInputChoiceNumberContact = int(input('Informe o numero da opção do telefone para deletar: '))

        lastContactsName = ''
        countContatcts = 0
        for contactsName in agenda:

            if lastContactsName == userInputChoiceContactName:
                countContatctsNumber = 1
                for contactsNumber in contactsName:
              
                    if countContatctsNumber == userInputChoiceNumberContact:
                        del agenda[countContatcts][countContatctsNumber - 1]
        
                    countContatctsNumber += 1
                    
            countContatcts += 1
            lastContactsName = contactsName

    elif userInputChoice == '4':
        
        userInputChoiceContactName = input('Informe o nome do contato: ')
        
        lastContactsName = ''
        for contactsName in agenda:
            cont = 1
            if lastContactsName == userInputChoiceContactName:
                for contactsNumber in contactsName:
                    print(f'\t{cont}° número: {contactsNumber}')
                    cont += 1
            lastContactsName = contactsName

        print()

    elif userInputChoice == '5':

        printNameContact = True
        for contactsName in agenda:
            if printNameContact:
                print(f'Contato: {contactsName}')
                printNameContact = False
            else:
                cont = 1
                for contactsNumber in contactsName:
                    print(f'\t{cont}° número: {contactsNumber}')
                    printNameContact = True
                    cont += 1
            print()

    elif userInputChoice != 'FIM':
        print('Informe uma opção valida')