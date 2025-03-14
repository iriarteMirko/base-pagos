SELECT
	PERIODO, 
	AGENCIA, 
	CODCENT AS CC, 
	CONTRATO, 
	CLAVE AS CARTERA, 
	FOCO AS PRIORIDAD, 
	CAPITALSOLES AS CAPITAL, 
	PAGOEFECTTOTALSOLESAGENCIACONT AS RECUPERO, 
	SEGMENTO_RIESGO AS SEGMENTO, 
	AMBITO_RCD_FINAL AS PRODUCTO, 
	INTENSIDAD AS INTENSIDAD_TOTAL, 
	DIRECTO_CALL AS INTENSIDAD_DIRECTA, 
	COBERTURA,
	--CONTACTO_EFECTIVO AS CONTACTO_DIRECTO, 
	PDP, 
	--TASA_CIERRE, 
	PDP_CUMPLIDA
FROM FB.CENTROCOBRANZAS.DBO.PD_EFECTIVIDAD_TARDIA_HISTORICO
WHERE 1=1 
AND PERIODO ='202502' 
AND FECHA = (SELECT MAX(FECHA)
			FROM FB.CENTROCOBRANZAS.DBO.PD_EFECTIVIDAD_TARDIA_HISTORICO
			WHERE PERIODO ='202502')
--AND CODCENT = '24825925'

/*
SELECT *
FROM FB.CENTROCOBRANZAS.DBO.PD_EFECTIVIDAD_TARDIA_HISTORICO
WHERE PERIODO ='202502'
*/

/*
SELECT MAX(FECHA) as FECHA_ACTUALIZACION
FROM FB.CENTROCOBRANZAS.DBO.PD_EFECTIVIDAD_TARDIA_HISTORICO
WHERE PERIODO ='202503'
*/

/*
SELECT *
FROM FB.CENTROCOBRANZAS.DBO.PD_EFECTIVIDAD_TARDIA_HISTORICO
WHERE 1=1 
AND PERIODO ='202502' 
AND FECHA = (SELECT MAX(FECHA)
			FROM FB.CENTROCOBRANZAS.DBO.PD_EFECTIVIDAD_TARDIA_HISTORICO
			WHERE PERIODO ='202502')
*/