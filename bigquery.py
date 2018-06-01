#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Query the BigQuery public table for the Metropolitan Art. """
from __future__ import absolute_import
import uuid

from google.Cloud import bigquery


def query_metart():
    # Specify your Google Cloud project to connect to
    client = bigquery.Client(project="whatsart1995")

    query_job = client.query("""
        #standardSQL
        SELECT object_name,department,culture,object_date,artist_display_name ,link_resource
        FROM `bigquery-public-data.the_met.objects`
        WHERE culture IS NOT NULL""")

    results = query_job.result()  # Waits for job to complete.

    for row in results:
        print(row[0:3])

if __name__ == '__main__':
    query_metart()
# [END all]
