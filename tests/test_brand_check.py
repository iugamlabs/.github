"""确认兼容例外只覆盖模块前缀，不能放过同一行的新旧组织链接。"""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('check_brand', Path(__file__).resolve().parents[1]/'scripts/check-brand.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)
OLD = 'star' + '-plan'

class BrandCheckTests(unittest.TestCase):
    def test_legacy_brand_and_repository_rejected(self):
        for text in ['Star'+' Plan', f'https://github.com/{OLD}/tool']:
            self.assertTrue(check.violations('README.md', text))

    def test_exact_compatibility_module_is_allowed(self):
        for text in [f'go install github.com/{OLD}/wechatctl/cmd/wxctl@latest', 'module github.com/heyoungai'+'/ship']:
            self.assertEqual(check.violations('README.md', text), [])

    def test_same_line_other_legacy_reference_is_rejected(self):
        self.assertTrue(check.violations('README.md', f'github.com/{OLD}/wechatctl github.com/{OLD}/other'))

    def test_module_prefix_cannot_hide_different_repository(self):
        self.assertTrue(check.violations('README.md', f'github.com/{OLD}/wechatctl-other'))

    def test_history_and_migration_examples_remain_allowed(self):
        for path in ['docs/migration.md','docs/changes/2026-09-10-release-plan.md','docs/releases/v1.0.0.md']:
            self.assertEqual(check.violations(path, OLD), [])

    def test_active_plans_are_checked(self):
        self.assertTrue(check.violations('docs/changes/active/distribution.md', OLD))

if __name__ == '__main__':
    unittest.main()
