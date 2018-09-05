# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class QueryExecutionResult(Model):
    """Describes query analysis results for execution in source and target.

    :param query_text: Query text retrieved from the source server
    :type query_text: str
    :param statements_in_batch: Total no. of statements in the batch
    :type statements_in_batch: long
    :param source_result: Query analysis result from the source
    :type source_result: ~azure.mgmt.datamigration.models.ExecutionStatistics
    :param target_result: Query analysis result from the target
    :type target_result: ~azure.mgmt.datamigration.models.ExecutionStatistics
    """

    _attribute_map = {
        'query_text': {'key': 'queryText', 'type': 'str'},
        'statements_in_batch': {'key': 'statementsInBatch', 'type': 'long'},
        'source_result': {'key': 'sourceResult', 'type': 'ExecutionStatistics'},
        'target_result': {'key': 'targetResult', 'type': 'ExecutionStatistics'},
    }

    def __init__(self, query_text=None, statements_in_batch=None, source_result=None, target_result=None):
        super(QueryExecutionResult, self).__init__()
        self.query_text = query_text
        self.statements_in_batch = statements_in_batch
        self.source_result = source_result
        self.target_result = target_result