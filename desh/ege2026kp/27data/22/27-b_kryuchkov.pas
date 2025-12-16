## uses Turtle;
var t := Matrbyrow(ReadAllText('27a1.txt').ToReals(',').Batch(2));
DrawPoints(t.col(0), t.col(1));
var KL1 := t.Rows.Where(\(x,y) -> y>3);
var KL2 := t.Rows.Where(\(x,y) -> y<3);
var (k1x, k1y):=(0.0, 0.0);
var sumD := real.MaxValue;
foreach var (cx,cy) in KL1 do begin
	var sum1 := KL1.Sum(\(x,y) -> (cx-x)**2 + (cy-y)**2);
	if sum1 < sumD then 
      (sumD, k1x, k1y):=(sum1, cx, cy);
end;
8)	Для второго кластера другой способ – с помощью LINQ.
var (k2x,k2y) := KL2.OrderBy(\(cx,cy) -> 
                     KL2.Sum(\(x,y) -> (cx-x)**2+(cy-y)**2)).First;
	Всего лишь одна строка вместо шести.
9)	Вывести ответ к задаче.
Println( floor((k1x+k2x)/2*10000), floor((k1y+k2y)/2*10000) );
10)	Для файла Б поступаем аналогично: изменить и сохранить в файл 27B1.txt.
## uses Turtle;
var t := Matrbyrow(ReadAllText('27b1.txt').ToReals(',').Batch(2));
DrawPoints(t.col(0), t.col(1));
 
11)	Три кластера определяем визуально по значениям абсцисс. Первый – от 0 до 3, второй – от 4 до 7, третий – от 7 до 10. В случае более сложной пересекающейся структуры запросы корректируются несложно с указанием обеих координат. Ни одна точка не лежит на прямой x = 7. Поэтому указываем 7 в двух местах без проблем. Сохраняем три кластера. Будем нумеровать их от ноля, чтобы дальше не напутать с индексацией массивов.
var KL0 := t.Rows.Where(\(x,y) -> y in 0..3);
var KL1 := t.Rows.Where(\(x,y) -> y in 4..7);
var KL2 := t.Rows.Where(\(x,y) -> y in 7..10);
12)	Находим все центроиды. Заводить массивы ради трёх координат или сохранить в отдельные переменные – дело вкуса программиста. В этом варианте сделаем массивы вещественных чисел.
var (kx, ky) := (|0.0|*3, |0.0|*3);
(kx[0],ky[0]) := KL0.OrderBy(\(cx,cy) -> 
                   KL0.Sum(\(x,y) -> (cx-x)**2+(cy-y)**2)).First;
(kx[1],ky[1]) := KL1.OrderBy(\(cx,cy) -> 
                   KL1.Sum(\(x,y -> (cx-x)**2+(cy-y)**2)).First;
(kx[2],ky[2]) := KL2.OrderBy(\(cx,cy) -> 
              KL2.Sum(\(x,y) -> (cx-x)**2+(cy-y)**2)).First;
13)	Вывести ответ для массивов проще.
Println(floor(kx.Average*10000), floor(ky.Average*10000));
