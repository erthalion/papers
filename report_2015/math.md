# Постановка задачи и математическая модель

Искусственные сердечные клапаны являются одними из самых сложных
аппаратов, применяемых в кардио-хирургии, т.к. существует множество факторов,
влияющих на их работу. Помимо этого, они должны удовлетворять
большому количеству условий, для того, чтобы быть безопасными и надежными
в использовании. Одними из самых важных аттрибутов искусственного сердечного клапана,
которые необходимо отразить в математической модели, являются следующие:

* Сложная неоднородная структура крови
* Высокая гибкость и подвижность лепестков клапана, а также их чрезвычайно малая толщина
* Необходимость определять напряжение деформации, возникающее на поверхности клапана в процессе его работы

## Структура крови и ее моделирование

Как известно, кровь состоит на 55% из плазмы и на 45% из форменных элементов, и в совокупности является
неньютоновской жидкость. Однако, как показано в [@whitmore1968rheology], отдельно плазма ведет себя как 
ньютоновская жидкость. При этом, реологические свойства крови очень зависят от скорости сдвига (shear rate),
и для большей части сердечного цикла в артериях и желудочках сердца его величина превышает пороговое значение
$50\; \text{сек}^{-1}$, поэтому кровь может рассматриваться как ньютоновская жидкость.

Используя все выше сказанное, а так же тот факт, что размеры частиц, входящих в форменные элементы
(лейкоциты, эритроциты и проч.) достаточно малы относительно размеров исследуемых сосудов
(например, диаметр эритроцита $\sim 6 \cdot 10^{-9}\text{м}$, а диаметр аорты $\sim 3 \cdot 10^{-2}\text{м}$),
мы будем моделировать кровь как вязкую несжимаемую неоднородную жидкость, состоящую
из двух компонент (главной компоненты - плазмы, и примеси - форменных элементов),
а течение жидкости - с помощью нестационарной системы дифференциальных уравнений Навье-Стокса.

$$\frac{\partial \vec{u}}{\partial t} + (\vec{u} \cdot \nabla) \vec{u} = - \frac{1}{\rho} \nabla p + \nabla \sigma + \vec{f}$$ {#eq:navier_stokes:motion}

$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{u}) = 0$$ {#eq:navier_stokes:continuity}

с начальными и краевыми условиями:

$$\vec{u}(\bar{x}, 0) = \vec{u}_0 \qquad \vec{u}|_{\Gamma_1, \Gamma_4} = \vec{u}_b \qquad u_{\Gamma_2, \Gamma3} = 0$$ {#eq:navier_stokes:velocity_conditions}

$$p_{\Gamma_2} = p_{in} \qquad p_{\Gamma_3} = p_{out}$$ {#eq:navier_stokes:pressure_conditions}

где $\bar{x}=(x,y,z) \in \Omega$,
$\vec{u}=(u,v,w)$ - вектор скорость, $u, v,
w$ - $x$-, $y$-, $z$-компонента вектора скорости,
$\vec{u}_b$ - скорость движения лепестков клапана под воздействием деформации,
$\rho=\rho(\bar{x}, t)$ - плотность,
$p=p(\bar{x}, t)$ - давление,
$\sigma = \mu (\nabla \vec{u} + (\nabla \vec{u})^T)$ - вязкий тензор напряжений,
$\mu = \mu(\bar{x}, t)$ - вязкость жидкости,
$\vec{f} = \vec{f}(\bar{x}, t)$ - вектор массовых сил.
Область $\Omega$ представляет собой сосуд с границами
$\Gamma = \Gamma_1 \cup \Gamma_2 \cup \Gamma_3 \cup \Gamma_4$, где
$\Gamma_1$ - стенки кровеносного сосуда,
$\Gamma_2$ and $\Gamma_3$ - области втекания/вытекания,
$\Gamma_4$ - лепестки клапана (см рис. \ref{fig:aorta_valve_scheme}).

![Схема расчетной области\label{fig:aorta_valve_scheme}](aorta_valve_scheme.png)

Как показано в [@gummel2013motion], для того, чтобы моделировать движение неоднородной жидкости (плазма и примеси), можно
добавить к системе уравнений ([@eq:navier_stokes:motion]), ([@eq:navier_stokes:continuity]) уравнение переноса концентрации:

$$\frac{\partial c}{\partial t} + \vec{u} \cdot \nabla c = 0$$ {#eq:convection}

с начальными условиями:

$$c(\bar{x}, 0) = c_0(\bar{x}), \bar{x} \in \Omega$$ {#eq:convection:conditions}

с краевыми условиями для области втекания:

$$c(\bar{x}, t)|_{\Gamma_2} = c_s(\bar{x}, t)$$ {#eq:convection:conditions}

и связать переменную плотность и вязкость с концентрацией примеси следующими линейными соотношениями:

$$\mu = c (\mu_2 - \mu_1) + \mu_1$$ {#eq:viscosity}

$$\rho = c (\rho_2 - \rho_1) + \rho_1$$ {#eq:density}

Т.о. мы получим математическую модель течения крови, которая отражает ее сложную структуру,
а также позволяет легко расширить это описание для описания большего количества компонент
и более сложных условий зависимости плотности и вязкости от концентрации.

## Моделирование эластичных лепестков клапана

Для того, чтобы построить модель, удовлетворяющую оставшимся требованиям, воспользуемся методом погруженной границы.
Метод погруженной границы используется для описания систем "жидкость-препятствие",
где эластичное препятствие погружено в вязкую несжимаемую жидкость.
Впервые был предложен в работе [@peskin2002immersed] для моделирования механики сердечных клапанов и потока крови в них.
Суть метода заключается в том, что при обтекании какого-либо тела жидкостью,
она испытывает влияние сил по направлению нормали к поверхности тела [@goldstein1993modeling].
Обтекаемое тело также испытывает влияние этих сил с противоположным знаком. Поэтому моделирование обтекания препятствия потоком жидкости возможно
с помощью формирования соответствующего поля внешних массовых сил в уравнении Навье-Стокса.
Это позволяет производить вычисления на простых прямоугольных сетках, которые могут не соответсвовать
геометрии расчетной области, что является одной из основных отличительных особенностей метода.

Данный подход был выбран по следующим причинам:

* возможность задавать сколь угодно тонкие лепестки клапана
* возможность моделировать чрезвычайно эластичные структуры, которые сильно меняют свою геометрию со временем
* легкость совмещения с имеющимся комплексом для расчета течения вязкой несжимаемой жидкости

Под термином "метод погруженной границы" обычно понимают как математическую формулировку,
так и схему для численного решения полученной задачи. "Погруженной границей" в данном контексте
обозначают любое гибкое препятствие, погруженное в жидкость. В данной работе под этим будем подразумевать
стенки кровеносного сосуда, а также лепестки клапана, расположенные внутри.
В дальнейшем, если не указано отдельно, будем описывать его только в применении к эластичным лепесткам клапана,
однако это без изменений может быть применено и к любым другим исследуемым объектам (например, фиброзному кольцу или стенкам кровеносного сосуда).

Существует также множество модификаций этого метода (например, метод погруженного интерфейса,
метод декартовых сеток, метод фиктивных ячеек, метод усеченных ячеек, см. [@mittal2005immersed],
но указаные методы не рассматриваются в данной работе.

Математическую формулировку этого метода и численную схему можно разделить на три раздела:

* Моделирование течения вязкой несжимаемой жидкости
* Моделирование деформации погруженной границы
* Моделирование взаимодействия между жидкостью и погруженной границей

Течение вязкой несжимаемой жидкости описывается системой нелинейных дифференциальных уравнений Навье-Стокса (см. предыдущий раздел)
в прямоугольной области $\tilde{\Omega}$, которая включает в себя расчетную область $\Omega$. Погруженная граница представлена в виде
набора упругих безмассовых волокон, имеющих "нейтральную плавучесть" \cite{griffith2012immersed},
расположение которых описано в лагранжевых координатах, а эластичность описана в терминах функционала
энергии деформации. Взаимодействие осуществляется исходя из того, что погруженная граница движется под давлением
жидкости с той же скоростью, что и сама жидкости, а внешние массовые силы в уравнении Навье-Стокса определяются
поверхностным напряжением, возникшим в результате деформации погруженной границы.

### Моделирование деформации погруженной границы

Опишем погруженную границу как гибкий несжимаемый материал, который расположен в области $\tilde{\Omega}$,
где $(q, r, s) = \bar{q}$ - криволинейные координаты связанные с материалом так, что зафиксированное значение
$(q, r, s)$ обозначает одну точку этого материала. Пусть $X(q, r, s, t) = X(\bar{q}, t)$ - позиция в декартовых координатах
точки, обозначенной $(q, r, s)$ в момент времени $t$. Тогда обобщая, $X(\bar{q}, t)$ описывает пространственную
конфигурацию всей погруженной границы в момент времени $t$, которая определяет соответствующую энергию деформации
$E[X(\bar{q}, t)]$ в момент $t$. Рассмотрим возмущение $\wp X(\bar{q}, t)$ конфигурации $X(\bar{q}, t)$,
где $\wp$ - оператор возмущения.
%NOTE: перевести точнее, "up to terms of first order" - с точностью первого порядка?
Результирующая деформация упругой энергии, возникшая в результате этого возмущения,
есть линейная функция от возмущения конфигурации, поэтому она может быть записана в форме:

$$\wp E[X(\bar{q}, t)] = \int_{\tilde{\Omega}} (-F(\bar{q}, t)) \cdot \wp X(\bar{q}, t)\; d\bar{q}$$ {#eq:elastic_energy_functional}

где $-F(\bar{q}, t)$ - производная Фреше от $E$, вычисленная для конфигурации $X(\bar{q}, t)$. Физически $F$
можно интепретировать, как плотность силы, которая создается путем деформирования погруженной границы.

Введем два вида погруженных границ:

* Неподвижная или малоподвижная граница
* Гибкая граница 

С помощью неподвижной границы будем моделировать фиксированные участки $\Gamma$, например, фиброзное кольцо,
к которому крепятся лепестки клапана, или стенки кровеносного сосуда, в том случае, если нас не интересуют
их деформации. Гибкие границы предназначены для моделирования подвижных участков $\Gamma$, которые испытывают
наибольшие деформации, например, лепестки клапана. Описанные типы границ обладают разными характеристиками, поэтому
для их описания мы будем использовать разные модели.

Для случая неподвижной границы мы можем использовать простую формулу, выражающую силу $F$ через смещение границы
в момент $t$ относительно исходного положения в момент $t_0$:

$$F = k \| X(\bar{q}, t_0) - X(\bar{q}, t) \|$$ {#eq:simple_force}

где $k$ - коэффициент жесткости.

Формула ([@eq:simple_force]) не подходит для гибких границ, т.к. позволяет учитывать только небольшие деформации.
Соответствующее уравнение для них может быть получено исходя из следующих соображений.
Как было сказано выше, погруженная граница представлена набором волокон.
Для того, чтобы определить $E$, удобно выбирать лагранжевые координаты $(q, r, s)$ так,
что каждое значение $(q, r)$ параметрически задает какое-либо одно конкретное волокно $s \to X(q^0, r^0, s)$.
В этом случае функционал упругой энергии $E$ можно представить в виде $E = E_s + E_b$,
где $E_s$ - энергия растяжения волокна, $E_b$ - энергия скручивания волокна,
а силу $F$, созданную благодаря деформации, в виде $F = F_s + F_b$.

Как показано в [@peskin2002immersed], [@griffith2009simulating] функционал энергии растяжения можно записать в виде:

$$E_s = \int_{\tilde{\Omega}} \varepsilon_s \left(\left| \frac{\partial X}{\partial s} \right| \right) d\bar{q}$$ {#eq:stretching_energy_functional}

а силу $F_s$:

$$F_s = \frac{\partial}{\partial s} \varepsilon_s^{,} \left( \left| \frac{\partial X}{\partial s} \right| \right) \tau$$ {#eq:stretching_force_density}

где $\varepsilon_s$ - локальная энергия растяжения, $\tau$ - единичный тангенциальный вектор для выбранного волокна $s$.
Т.к. напряжение растяжения $T = \varepsilon_s^{,} \left( \left| \frac{\partial X}{\partial s} \right| \right)$, то уравнение ([@eq:stretching_force_density])
можно переписать в виде, который соответствует обобщенному закону Гука:

$$F_s = \frac{\partial}{\partial s} T \tau$$ {#eq:stretching_force_density_simplified}

Т.к. площать попреречного сечения сосудов достаточно мала по отношению к их длинне, для моделирования энергии напряжения и 
сил сопротивления скручиванию мы можем воспользоваться уравнением Эйлера-Бернулли [@gere1997mechanics]:

$E_b = \frac{1}{2} \int_{\tilde{\Omega}} k \cdot \left| \frac{\partial^2 X^0}{\partial s^2} - \frac{\partial^2 X}{\partial s^2} \right|^2 \; d\bar{q}$

$F_b = \frac{\partial^2}{\partial s} \left( k \cdot \left(\frac{\partial^2 X^0}{\partial s^2} - \frac{\partial^2 X}{\partial s^2} \right) \right)$

где $k = E \cdot I$, $E$ - модуль упругости, $I$ - момент инерции поперечного сечения, $\frac{\partial^2 X^0}{\partial s^2}$, $\frac{\partial X}{\partial s^2}$ -
отклонение погруженной границы от равновесного положения в начальный и текущий момент времени.

Таким образом, плотность силы $F$, создаваемая при деформации погруженной границы может быть выражена в виде:

$F = \frac{\partial}{\partial s} T \tau + \frac{\partial^2}{\partial s} \left( k \cdot \left(\frac{\partial^2 X^0}{\partial s^2} - \frac{\partial^2 X}{\partial s^2} \right) \right)$

### Моделирование взаимодействия

Как показано в [@peskin2002immersed], для того, чтобы описать взаимодействие потока жидкости и погруженной границы,
необходимо ввести в рассмотрение прямоугольную область $(x, y, z) = \bar{x} \in \tilde{\Omega}$, так что $\Omega \in \tilde{\Omega}$, а также
область $(q, r, s) = \bar{q} \in \Gamma$, которая соответствует точкам погруженной границы в лагранжевых координатах.
В этих областях запишем следующую систему уравнений:

$$\frac{\partial \vec{u}}{\partial t} + (\vec{u} \cdot \nabla) \vec{u} = - \frac{1}{\rho} \nabla p + \nabla \sigma + \vec{f}$$ {#eq:navier_stokes:ibm:motion}

$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{u}) = 0$$ {#eq:navier_stokes:ibm:continuity}

$$\frac{\partial X}{\partial t}(\bar{q}, t) = \int_{\Omega} \vec{u}(\bar{x}, t) \cdot \delta (x - X(\bar{q}, t))\; d\bar{x}$$ {#eq:interaction:velocity}

$$\vec{f}(\bar{x}, t) = \int_{\Gamma} \vec{F}(\bar{q}, t) \cdot \delta (x - X(\bar{q}, t))\; d\bar{q}$$ {#eq:interaction:force}

Уравнения (@[eq:navier_stokes:ibm:motion]), ([@eq:navier_stokes:ibm:continuity]) - это система уравнений Навье-Стокса,
которая используется для моделирования течения жидкости, и полностью записана в эйлеровых координатах $(x, y, z) \in \tilde{\Omega}$.
Уравнения [@eq:interaction:velocity], [@eq:interaction:force] являются уравнениями взаимодействия жидкости с погруженной границей
и позволяет переходить от эйлеровых к лагранжевым координатам. В уравнениях ([@eq:interaction:velocity]), ([@eq:interaction:force])
$\delta$ - дельта функция Дирака, $F$ - плотность силы деформации, описанная в предыдущем разделе \textbf{Моделирование деформации погруженной границы}.

Подробное доказательство системы уравнений ([@eq:navier_stokes:ibm:motion]) - ([@eq:interaction:force]) опубликовано в \cite{peskin2002immersed}.
В данной работы мы приведем его краткое описание. Рассмотрим более обший случай,
когда гибкий несжимаемый материал заполняет всю область $\tilde{\Omega}$, т.е. $\tilde{\Omega} = \Gamma$.
Исходя из принципа наименьшего действия, на временном промежутке $(0, T)$ система должна развиваться так, чтобы достигался минимум:

$S = \int_0^T L(t) dt$

где $L(t)$ - разница между кинетической и потенциальной энергией, в нашем случае:

$$L(t) = \frac{1}{2} \int \left| \frac{\partial X}{\partial t}(\bar{q}, t) \right|^2 \; d\bar{q} - E(X(\bar{q}, t))$$ {#eq:least_action}

Т.о. для любого возмущения $\wp X$ требуется:

$0 = -\wp S = \int_0^T \int \left( \frac{\partial^2 X}{\partial t^2} - F \right) \cdot \wp X \; d\bar{q} \; dt$

Вводя в рассмотрение скорость жидкости $u$ и скорость деформации $U$:

$u(X(\bar{q}, t), t) = \frac{\partial X}{\partial t}(\bar{q}, t)$

$U(X(\bar{q}, t), t) = \wp X(\bar{q}, t)$

можно показать, что $\wp X$ удовлетворяет условию несжимаемости в лагранжевых координатах, и можно записать следующие уравнения:

$\wp X(\bar{q}, t) = \int U(\bar{x}, t) \; \delta(\bar{x} - X(\bar{q}, t)) d\bar{x}$

$\frac{\partial^2 X}{\partial t^2} \cdot \wp X(\bar{q}, t) = \int  \left(\frac{\partial u}{\partial t} + u \cdot \triangle u \right) U(\bar{x}, t) \; \delta(\bar{x} - X(\bar{q}, t)) d\bar{x}$

Подставляя эти формулы в ([@eq:least_action]) получим:

$0 = \int_0^T \int \int \left( \frac{\partial u}{\partial t} + u \cdot \triangle u - F(\bar{q}, t) \right) \cdot U(\bar{x}, t) \; \delta(\bar{x} - X(\bar{q}, t)) \; d\bar{x} \; d\bar{q} \; dt$

Произведя замену

$f(x, t) = \int F(\bar{q}, t) \; \delta(\bar{x} - X(\bar{q}, t)) \; d\bar{q}$

после ряда преобразований можно завершить переход от лагранжевых переменных к эйлеровым.

Помимо этого, в [@peskin2002immersed] показано, что несмотря на отсутствие предположений
о неоднородности плотности жидкости, уравнение:

$\frac{\partial \rho}{\partial t} + u \cdot \triangle \rho = 0$

есть следствие приведенной системы уравнений. Метод погруженной границы является следствием описанного случая,
в котором эластичный несжимаемый материал заполняет не всю область $\tilde{\Omega}$, а только часть, и представляет
собой поверхность, погруженную в жидкость.

# Список литературы