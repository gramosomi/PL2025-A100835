program WhileLoop;
var
  i, sum: integer;
begin
  i := 1;
  sum := 0;
  while i <= 5 do
  begin
    sum := sum + i;
    i := i + 1;
  end;
  writeln('Sum from 1 to 5 is: ', sum);
end.
