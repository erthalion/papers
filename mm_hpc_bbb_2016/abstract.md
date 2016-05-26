# MATHEMATICAL MODELLING OF ARTIFICIAL HEART VALVE PERFORMANCE

D.A. Dolgov, Y.N. Zakharov
Kemerovo State University, Kemerovo, Russia
e-mail: 9erthalion6@gmail.com

Keywords: viscous inhomogeneous fluid, artificial heart valve, immersed boundary method

Motivation and Aim: In recent years interest in mathematical modeling of blood
flow in vessels and artificial human heart valves significantly increased
because of development of new methods of cardiovascular system diseases
treatment. An artificial heart valve is an extremely complex system, which must
meet a number of requirements, and mathematical modeling can simplify valve
development and optimization process. In this paper we propose the mathematical
model and its numerical implementation to describe three dimensional blood flow
dynamics in artificial heart valve and its numerical implementation.

Methods and Algorithms:

Acknowledgements: The research is performed as part of the government contract
1.630.1.2014/K.

References: 

Предложенная для решения нестационарной задачи о течении крови внутри клапана
математическая модель позволяет учитывать основные особенности функционирования
сердечного клапана: неоднородную структуру крови, а также гибкость лепестков
клапана, их сложную форму и чрезвычайную тонкость. Кровь моделируем как вязкую
несжимаемую неоднородную жидкость, состоящую из двух компонент
(соответствующих, например, плазме и форменным элементам). Ее движение описываем с помощью
нестационарной системой дифференциальных уравнений Навье-Стокса с переменными
вязкостью и плотностью, где концентрация примеси описывается уравнением
конвекции. Лепесток клапана моделируем как гибкую непроницаемую поверхность,
которая деформируется под воздействием давления крови. Деформацию лепестков, а
также их взаимодействие с жидкостью описываем с помощью метода погруженной
границы, учитывая влияние лепестков на течение с помощью добавления массовых
сил в уравнение движения жидкости.

Описанная математическая модель и численный метод решения могут быть применены
для решения широкого круга медицинских задач. Задавая в качестве начальных
данных перепад давления, форму сосуда и лепестков клапана, а также начальное
распределение примесей в крови, можно определить динамику описанной
биологической системы, включая расход жидкости в сосуде, геометрию лепестков
клапана и их напряжение деформации в любой момент времени и распределение
примеси в крови.
