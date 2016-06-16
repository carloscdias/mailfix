#!/usr/bin/python3
import sys
import re

qwerty_layout = {
	'a': 'qwsxz',
	'b': 'vghn',
	'c': 'xdfv',
	'd': 'serfcx',
	'e': 'wsdrf',
	'f': 'dcvgtre',
	'g': 'fvbhytr',
	'h': 'gbnjuyt',
	'i': 'ujklo',
	'j': 'hnmkiuy',
	'k': 'jm,loiu',
	'l': 'k,.çpoi',
	'm': 'njk,',
	'n': 'bhjm',
	'o': 'iklçp',
	'p': 'olç',
	'q': 'asw',
	'r': 'edfgt',
	's': 'azxdewq',
	't': 'rfghy',
	'u': 'yhjki',
	'v': 'cfgb',
	'w': 'qasde',
	'x': 'zsdc',
	'y': 'tghju',
	'z': 'asx'
}

def replace_cost( char1, char2 ):
	if char1 == char2:
		return 0

	if char1 in qwerty_layout and char2 in qwerty_layout[ char1 ]:
		return 1

	return 2

# preço a ser pago para a string1 se transformar na string2
def edit_distance( string1, string2, memo, insert_cost = 1, delete_cost = 1, transp_cost = 1, LARGE_VALUE = 9999 ):
	if not string1:
		return ( len( string2 ) * insert_cost )

	if not string2:
		return ( len( string1 ) * delete_cost )

	memo_key = string1 + string2

	if memo_key in memo:
		return memo[ memo_key ]

	replace = replace_cost( string1[0], string2[0] ) + edit_distance( string1[1:], string2[1:], memo )
	insert  = insert_cost + edit_distance( string1, string2[1:], memo )
	delete  = delete_cost + edit_distance( string1[1:], string2, memo )
	transpo = ( transp_cost + replace_cost( string1[1], string2[0] ) + edit_distance( string1[0] + string1[2:], string2[1:], memo ) ) if len( string1 ) >= 2 else LARGE_VALUE

	memo[ memo_key ] = min( replace, insert, delete, transpo )
	
	return memo[ memo_key ]

def processar_semelhanca( dominios_ordenados, confianca, dominios, grau_semelhanca ):
	mapeamento                        = {}

	recuperados                       = 0
	dominios_adicionados              = 0
	total_emails_dominios_adicionados = 0

	for dominio_errado in dominios_ordenados[confianca:]:
		
		mapeamento[ dominio_errado ], minimo = dominio_errado, grau_semelhanca + 1
		
		for dominio_certo in dominios_ordenados[:confianca]:
			temp   = edit_distance( dominio_errado, dominio_certo, {} )
			if temp < minimo:
				minimo = temp
				mapeamento[ dominio_errado ] = dominio_certo
		
		if mapeamento[ dominio_errado ] != dominio_errado:
			print( '{0:20s} -> {1:20s}'.format( dominio_errado, mapeamento[ dominio_errado ] ) )
			recuperados += dominios[ dominio_errado ]
		else:
			dominios_adicionados += 1
			total_emails_dominios_adicionados += dominios[ dominio_errado ]

	print( '{0} emails recuperados'.format( recuperados ) )
	print( '{0} domínios adicionados totalizando {1} emails'.format( dominios_adicionados, total_emails_dominios_adicionados ) )
	return mapeamento

def Main():
	if len( sys.argv ) < 3:
		raise SystemExit( '{0} <lista-emails> <lista-corrigida>'.format( sys.argv[0] ) )

	# http://emailregex.com/
	regex_email = re.compile( r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)' )

	removidos   = []
	dominios    = {}

	total_linhas = 0
	total_emails = 0
	lista_emails = []

	with open( sys.argv[1] ) as arquivo_emails:

		for linha in iter( arquivo_emails.readline, '' ):
			linha   = linha.lower().strip( '"\n ' )
			indice  = linha.find( '@' )

			if regex_email.match( linha ):
				dominio = linha[( indice + 1 ): ]
				dominios[ dominio ] = ( dominios[ dominio ] if dominio in dominios else 0 ) + 1
				lista_emails.append( { 'nome': linha[:indice], 'dominio': dominio } )
				total_emails += 1
			else:
				removidos.append( linha )

			total_linhas += 1

	print( 'Terminada leitura do arquivo' )
	print( '{0} linhas processadas, {1} possíveis e-mails, {2} linhas removidas'.format( total_linhas, total_emails, len( removidos ) ) )
	
	if removidos:
		print( '-- Removidos\n{0}\n'.format( '\n'.join( removidos ) ) )
	
	top = 10

	print( 'Ordenando {0} domínios distintos pelo número de usuários inscritos e selecionando os top\'s {1} como corretos'.format( len( dominios ), top ) )
	dominios_ordenados = sorted( dominios, key = dominios.get, reverse = True )
	
	print( 'Primeiros {0} domínios com maior número de usuários inscritos'.format( top ) )

	total_corretos = 0
	for dominio in dominios_ordenados[:top]:
		print( '{0:20s} - {1:7d} usuários'.format( dominio, dominios[ dominio ] ) )
		total_corretos += dominios[ dominio ]

	print( '{0} correspondendo a {1:0.2f}% de emails considerados como certos'.format( total_corretos, 100 * total_corretos / total_emails ) )
	print( 'Processando semelhança entre {0} ({1:0.2f}%) emails restantes...'.format( total_emails - total_corretos, 100 * ( 1 - total_corretos / total_emails ) ) )
	
	mapeamento = processar_semelhanca( dominios_ordenados, top, dominios, 2 )

	for dominio in dominios_ordenados[:top]:
		mapeamento[ dominio ] = dominio
	
	print( 'Escrevendo arquivo...' )

	with open( sys.argv[2], 'w' ) as lista_corrigida:
		for email in lista_emails:
			lista_corrigida.write( '{0}@{1}\n'.format( email['nome'], mapeamento[ email['dominio'] ] ) )

	print( 'Operação concluída' )

if __name__ == '__main__':
	Main()
