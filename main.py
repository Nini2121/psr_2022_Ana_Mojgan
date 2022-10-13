#para os argumentos iniciais dos limites
import argparse
#para a criaçãode uma letra random
import random
#para a contagem do tempo no programa
from time import time
from time import time,ctime
#colorir as letras segundo a correção do typing test
import colorama
from colorama import Fore, Back, Style
#para ler os caracteres do teclado
from readchar import readkey, key
#formação de namedtuples
from collections import namedtuple
#originar o dicionario com uma impressão mais percetível
from pprint import pprint



#função para a definição dos limites do código e das condições iniciais
def arg():
    parser = argparse.ArgumentParser(description='Typing test from Ana and Mojgan')
    parser.add_argument('-utm', '--use_time_mode', dest='use_time_mode', action='store_true', help= "Max number of secs for time mode or maximum number of inputs for number of inputs mode")
    parser.add_argument('-mv Max_VALUE', '--max_value', dest='max_value', type=int, required=True, help= "Max number of seconds for time mode or maximum number of inputs for number of inputs mode")
    parser.set_defaults(use_time_mode=False)
    args = parser.parse_args()
    print(vars(args))
    return vars(args)




#função para a geração de uma letra random minúscula
def randLetter():
    randomLowerLetter= chr(random.randint(ord('a'), ord('z')))

    return randomLowerLetter

#funções para deixar uma mensagem final ao participante
def msg(timer, values):
    if timer >= values:
        print('Current test duration: ' + str(timer) + ' seconds- above the expected time!(' +str(values)+ ' seconds)')
        print(Fore.CYAN + 'GOOD JOB, THE TEST IS FINISHED! :)')
    else:
        print(Fore.CYAN + 'SAD U QUIT',end='\n')

def msg2(counter, values):
    if counter >= values:
        print('You spent all of your ' +str(values)+ ' tries')
        print(Fore.CYAN + 'GOOD JOB, THE TEST IS FINISHED! :)')
    else:
        print(Fore.CYAN + 'SAD U QUIT',end='\n') #ver


 

#onde irão decorrer o typing test assim como a recolha dos parâmetros pedidos
def typeTest(value1,value2):    
    list_tuple=[]
    Input=namedtuple('Input',['requested','received','duration'])
    program_ti=time()
    test_start=ctime()
    list_request=[]
    list_received=[]
    duration_list=[]


    if value1 ==True: 
        print('Test running up to '+ str(value2) + 'seconds')
        print('Type any lowercase letter to start your test:')
        readkey()
        
        start=time()
        timer=0

        
        
        while timer <= value2:
           
            end=time()
            timer=end-start
            

            letra=randLetter()
            list_request.append(letra)
        
            print('Type letter '+ letra)
            start_input=time()
            print('you type:', end=" ")
            resposta = readkey()
            list_received.append(resposta)
            end_input=time()
            
            
            duration=end_input-start_input
            duration_list.append(duration)
           


            list_tuple.append(Input(letra, resposta, duration))
            if resposta == ' ':
                
                break

            if resposta==letra:
                print(Fore.GREEN + resposta)
            else:
                print(Fore.RED + resposta)
        mensagem_final=msg(timer,value2)


    else:
        print('Test running up to '+ str(value2) + ' tries')
        print('Type any lowercase letter to start your test:')
        readkey()
        counter=0
        while counter<= value2:
            counter=counter+1


            letra=randLetter()
            list_request.append(letra)
            
            print('Type letter '+ letra)
            start_input=time()
            print('you type:', end=" ")
            resposta = readkey()
            list_received.append(resposta)
            end_input=time()

            duration=end_input-start_input
            duration_list.append(duration)
            

            list_tuple.append(Input(letra, resposta, duration))
            
            if resposta == ' ':
                
                break

            if resposta==letra:
                print(Fore.GREEN + resposta)
            else:
                print(Fore.RED + resposta)
    

        mensagem_final=msg2(counter, value2)
    
    program_tf=time()

    test_duration=program_tf-program_ti 

    test_end=ctime() 
    parameters=[test_duration, test_start, test_end, list_request, list_received, duration_list, list_tuple] 
    print(list_request)
    return parameters
        

def parametros(parameters):
    #numero de input correto
    list_request=parameters[3]
    list_received=parameters[4]
    duration_list=parameters[5]
    

    duration_correct_list=[]
    duration_miss_list=[]
    number_of_hits=0
    number_of_elements=len(list_request)


    for i in range(number_of_elements):
        if list_request[i]==list_received[i]:
            number_of_hits=number_of_hits+1
            duration_correct_list.append(duration_list[i])
        else:
            duration_miss_list.append(duration_list[i])

            
    #numero total de inputs

    number_of_types=len(list_request)

    #accurcy
    accuracy=number_of_hits/number_of_types
   
    #type_average_duration
    total_time=0
    for i in parameters[5]:
        total_time=total_time+i

    type_average_duration=total_time/len(parameters[5])

    #type_hit_average_duration
    total_hit_time=0
    for i in duration_correct_list:
        total_hit_time=total_hit_time+i
    
    type_hit_average_duration=total_hit_time/len(duration_correct_list)

    #type_miss_average_duration
    total_miss_time=0
    for i in duration_miss_list:
        total_miss_time=total_miss_time+i
    
    type_miss_average_duration=total_hit_time/len(duration_miss_list)

    statistics=[accuracy,parameters[6],number_of_hits, number_of_types ,parameters[0], parameters[2], parameters[1], type_average_duration, type_hit_average_duration, type_miss_average_duration]


    return statistics

#criação do dicionario 
def dictionary(statistics):
    dictionary={'accuracy':statistics[0],'inputs':statistics[1], 'number_of_hits':statistics[2], 'number_of_types':statistics[3],'test_duration':statistics[4],'test_end':statistics[5],'test_start':statistics[6],'type_average_duration':statistics[7],' type_hit_average_duration':statistics[8],'type_miss_average_duration':statistics[9]}
    return dictionary



def main():
    values=arg()
    colorama.init(autoreset=True)
    test=typeTest(values.get('use_time_mode'),values.get('max_value'))
    Dic_parameters=parametros(test)
    my_dict=dictionary(Dic_parameters)
    pprint(my_dict)

    

if __name__ == "__main__":
    main()




