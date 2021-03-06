#    Copyright 2017 Cargill Incorporated
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from pipewrench import test_util

def test_kudu_table_count_sql():
    conf_string = '''---
    staging_database:
      name: test_db
    tables:
      - destination:
          name: destination'''

    expected = test_util.read_file('kudu-table-count.sql')
    actual = test_util.merge_single(conf_string, None, '../kudu-table-count.sql')

    assert actual == expected

def test_kudu_table_insert_sql():
    conf_string = '''---
    staging_database:
      name: test_db
    tables:
      - destination:
          name: destination
        check_column: col1
        columns:
          - name: col1
          - name: col2'''

    expected = test_util.read_file('kudu-table-insert.sql')

    actual = test_util.merge_single(conf_string, None, '../kudu-table-insert.sql')
    print(actual)
    assert actual == expected
