program SomaArray;
var
numeros: array[1..5] of integer;  {'numeros' não tem endereço definido.}
i, soma: integer;
begin
soma := 0;
writeln('Introduza 5 numeros inteiros:');
for i := 1 to 5 do
begin
readln(numeros[i]);
soma := soma + numeros[i];
end;
writeln('A soma dos números é: ', soma);
end.