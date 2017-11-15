#!/usr/bin/perl 

use CGI;
use DBI;

my $cgi = new CGI;

	my $base_datos="tp2"; 
	my $usuario="root"; 
	my $clave="fran"; 
	my $driver="mysql"; 

	my $dbh = DBI->connect("dbi:$driver:$base_datos",$usuario,$clave) or die "\nError al abrir 		la base datos: $DBI::errstr\n";


if(!$cgi->param){

    print $cgi->header(-charset => 'utf8');

    print $cgi->start_html('tp2');

    print $cgi->center;

    print $cgi->start_form(-onsubmit=>'/submit');

    print $cgi->h1('Ordenadores Alcón');

    print $cgi->h3('Introduzca los datos del ordenador que desea añadir');

    print $cgi->label('Modelo: ');

    print $cgi->textfield(-name=>'nombre',-size=>15,-maxlength=>50);

    print $cgi->br;

    print $cgi->br;

    print $cgi->label('Marca: ');

    print $cgi->textfield(-name=>'marca',-size=>15,-maxlength=>50);

    print $cgi->br;

    print $cgi->br;

    print $cgi->label('Precio: ');

    print $cgi->textfield(-name=>'precio',-size=>15,-maxlength=>50);
   
    print $cgi->br;

    print $cgi->br;

    print $cgi->label('Pais: ');

    print $cgi->popup_menu('pais',
			    ['Spain','France','England','Italy','Japan','China'],
			    'Spain');
    print $cgi->br;

    print $cgi->br;

    print $cgi->submit('submit','Añadir');
    
    print $cgi->br;

    print $cgi->br;

    print $cgi->reset('reset','Borrar campos');

    print $cgi->end_form;

	print $cgi->h1('Registros actuales: ');

	my $sth = $dbh->prepare("SELECT * FROM ordenadores;");

	 #Realizamos la etapa de ejecución de la sentencia
	 $sth->execute();

	 #Realizamos la etapa de extracción de datos. Imprimimos tupla a tupla.
	 while ( @tupla=$sth->fetchrow_array())
	 {
		print "Modelo: $tupla[0] - Marca: $tupla[1] - Precio: $tupla[2] - 
		País: $tupla[3]\n";

		print $cgi->br;

		print "-------------------------------------------------------------------------";

		print $cgi->br;

	 }

	 #Realizamos la etapa de liberación de recursos ocupados por la sentencia
	 $sth->finish();

    	print $cgi->center;

} else {

    print $cgi->header(-charset => 'utf8');

    print $cgi->start_html('Add MYSQL');

 #BD	
	
    my $nombre = $cgi->param('nombre');
    my $marca = $cgi->param('marca');
    my $precio = $cgi->param('precio');
    my $pais = $cgi->param('pais');

    print $cgi->h1('El siguiente registro fue insertado...');
    print $cgi->br;
    print "$nombre";
    print $cgi->br;
    print "$marca";
    print $cgi->br;
    print "$precio";
    print $cgi->br;
    print "$pais";
    print $cgi->br;

	my $base_datos="tp2"; 
	my $usuario="root"; 
	my $clave="fran"; 
	my $driver="mysql"; 

	my $dbh = DBI->connect("dbi:$driver:$base_datos",$usuario,$clave) or die "\nError al abrir 		la base datos: $DBI::errstr\n";

	my $sql = "INSERT INTO ordenadores(nombre,marca,precio,pais)
    		   VALUES(?,?,?,?)";

	$statement = $dbh->prepare($sql);

	$statement->execute($nombre, $marca, $precio, $pais);

	print $cgi->br;

	print $cgi->br;

	print "<br><a href='http://localhost/cgi-bin/form.cgi'>Volver al formulario</a>"

}

$dbh->disconnect or warn "\nFallo al desconectar.\nError: $DBI::errstr\n";



