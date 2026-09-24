-- 1. Top 5 funds by AUM
SELECT
    f.scheme_name,
    SUM(a.aum) AS total_aum
FROM fact_aum a
JOIN dim_fund f ON a.fund_id = f.fund_id
GROUP BY f.scheme_name
ORDER BY total_aum DESC
LIMIT 5;


-- 2. Average NAV by month
SELECT
    d.year,
    d.month,
    f.scheme_name,
    AVG(n.nav) AS average_nav
FROM fact_nav n
JOIN dim_fund f ON n.fund_id = f.fund_id
JOIN dim_date d ON n.date_id = d.date_id
GROUP BY d.year, d.month, f.scheme_name
ORDER BY d.year, d.month;


-- 3. SIP year-over-year growth
SELECT
    d.year,
    SUM(t.amount) AS sip_amount
FROM fact_transactions t
JOIN dim_date d ON t.date_id = d.date_id
WHERE LOWER(t.transaction_type) = 'sip'
GROUP BY d.year
ORDER BY d.year;


-- 4. Transactions by state
SELECT
    state,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;


-- 5. Funds with expense ratio below 1%
SELECT
    f.scheme_name,
    AVG(p.expense_ratio) AS expense_ratio
FROM fact_performance p
JOIN dim_fund f ON p.fund_id = f.fund_id
GROUP BY f.scheme_name
HAVING AVG(p.expense_ratio) < 1
ORDER BY expense_ratio;


-- 6. Average fund return
SELECT
    f.scheme_name,
    AVG(p.return_value) AS average_return
FROM fact_performance p
JOIN dim_fund f ON p.fund_id = f.fund_id
GROUP BY f.scheme_name
ORDER BY average_return DESC;


-- 7. Total transactions by transaction type
SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    SUM(amount) AS total_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_amount DESC;


-- 8. Average NAV by fund
SELECT
    f.scheme_name,
    AVG(n.nav) AS average_nav
FROM fact_nav n
JOIN dim_fund f ON n.fund_id = f.fund_id
GROUP BY f.scheme_name
ORDER BY average_nav DESC;


-- 9. Maximum NAV by fund
SELECT
    f.scheme_name,
    MAX(n.nav) AS maximum_nav
FROM fact_nav n
JOIN dim_fund f ON n.fund_id = f.fund_id
GROUP BY f.scheme_name
ORDER BY maximum_nav DESC;


-- 10. Minimum NAV by fund
SELECT
    f.scheme_name,
    MIN(n.nav) AS minimum_nav
FROM fact_nav n
JOIN dim_fund f ON n.fund_id = f.fund_id
GROUP BY f.scheme_name
ORDER BY minimum_nav;