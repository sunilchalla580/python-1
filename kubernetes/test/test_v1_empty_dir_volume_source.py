# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_empty_dir_volume_source import V1EmptyDirVolumeSource


class TestV1EmptyDirVolumeSource(unittest.TestCase):
    """ V1EmptyDirVolumeSource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1EmptyDirVolumeSource(self):
        """
        Test V1EmptyDirVolumeSource
        """
        model = kubernetes.client.models.v1_empty_dir_volume_source.V1EmptyDirVolumeSource()


if __name__ == '__main__':
    unittest.main()
