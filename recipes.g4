grammar recetas;

consulta       : condicion (OPERADOR_LOGICO condicion)* ;
condicion      : ingrediente | '(' consulta ')' ;
ingrediente    : cantidad? descriptor* PALABRA (descriptor+ PALABRA)* ;
cantidad       : NUMERO ;
descriptor     : PALABRA ;
PALABRA        : [a-zA-ZáéíóúÁÉÍÓÚñÑ]+ ;
NUMERO         : [0-9]+ ;
OPERADOR_LOGICO: ',' | '|' ;
WS             : [ \t\n\r]+ -> skip ;