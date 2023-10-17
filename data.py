fixtures = [
    {
        "title": "Поиск одинаковых и похожих изображений в базе данных на основе перцептивных хэш-строк",
        "author_id": 3,
        "body": "Хэширование изображений — одна из основных технологий в области безопасности мультимедиа. Данный метод использует последовательность фиксированной длины, состоящую из двоичных или действительных чисел, называемую хэшем изображения, для представления входного изображения и применяется в аутентификации изображений, обнаружении несанкционированного доступа, индексации изображений, поиске изображений на основе содержимого и обнаружении копий изображений.",
    },
    {
        "title": "Ранние методы хеширования изображений",
        "author_id": 1,
        "body": "Ранние методы хеширования изображений включают дискретное вейвлет-преобразование (DWT), дискретное косинусное преобразование (DCT) и работу с коэффициентами DCT.Venkatesan, R. в своей статье использует статистику вейвлет-коэффициентов, низкочастотные коэффициенты преобразования Фурье для построения хэша изображения, который устойчив к сжатию JPEG, медианной фильтрации и повороту не малые углы, но уязвим к гамма-коррекции и регулировке контраста. Так же недостатком этого метода является то, что известная вейвлет-статистика может быть использована для создания визуально другого изображения с тем же хэшем.Fridrich, J. и Goljan M. отмечают, что величину низкочастотного коэффициента DCT нельзя изменить, не вызывая видимых изменений изображения, таким образом, коэффициенты DCT могут сохранять информацию об изображении, и было предложено использовать их для создания хэшей изображений. Этот хэш устойчив к обычным манипуляциям, но чувствителен к повороту изображений. Lin Y. и Chang S. предлагают метод, использующий инвариантные соотношения между коэффициентами DCT в одной и той же позиции, но в разных отдельных блоках, так как обнаружили, что отношения между коэффициентами DCT в одной и той же позиции в отдельных блоках сохраняются до и после сжатия JPEG. Этот метод также может обрабатывать искажения, вызванные манипуляциями, такими как округление целых чисел, фильтрация изображений.",
    },
    {
        "title": "Перцептивные хеш-алгоритмы ",
        "author_id": 2,
        "body": "Перцептивное хеширование — это класс односторонних отображений мультимедийных презентаций в перцепционное хеш-значение с точки зрения их воспринимаемого содержания [14]. Результатом данного метода является цепочка битов, которая содержит информацию об исходном изображении. Полученные последовательности битов должны быть подобны друг другу для одинаковых или похожих изображений, к которым были подвергнуты геометрическим модификациям или цветокоррекции.",
    },
]
