import { test, expect } from '@playwright/test';

test('admin panel login smoke test', async ({ page }) => {
  await page.goto('https://example.com/login');
  await page.getByLabel('Email').fill('test@example.com');
  await page.getByLabel('Password').fill('Password123!');
  await page.getByRole('button', { name: 'Login' }).click();

  await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
});
