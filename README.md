### fixture -> setup + teardown

### :exclamation: `pytest test_google_duckduckgo.py --setup-plan`

#### В фикстурах используются `scope`, который позволяет указать, когда будет вызываться фикстура. Возможные значения:

`function` — фикстура будет вызываться перед каждым тестом. Это значение по умолчанию и можно не указывать его явно.

`class` — фикстура будет вызываться перед всеми тестами в классе. И если в классе несколько тестов, то фикстура будет вызываться один раз перед всеми тестами в классе и один раз после всех тестов в классе.

`module` — фикстура будет вызываться перед всеми тестами в модуле. Будет вызываться один раз перед всеми тестами в модуле и один раз после всех тестов в модуле.

`session` — фикстура будет вызываться перед всеми тестами в сессии. Будет вызываться один раз перед всеми тестами в сессии и один раз после всех тестов в сессии.

`package` — фикстура будет вызываться перед всеми тестами в пакете. Будет вызываться один раз перед всеми тестами в пакете и один раз после всех тестов в пакете.

### Если в фикстуре указать `autouse=True` то фикстура будет запускаться перед каждым тестом автоматически и в тестах не нужно будет указывать.
