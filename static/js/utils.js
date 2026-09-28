const MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

// Formats "2026-09-28" as "28 Sep 2026" without creating a Date object,
// so timezones cannot shift the day.
export function formatExpenseDate(dateString) {
const [year, month, day] = String(dateString).slice(0, 10).split("-");
const monthName = MONTH_NAMES[Number(month) - 1];

if (!year || !monthName || !day) return String(dateString); // unexpected format: show as-is
return `${day} ${monthName} ${year}`;
}

// export function formatExpenseDate(expenseDate) {
//     const today = new Date();
//     const expenseDateObject = new Date(expenseDate);

//     today.setHours(0, 0, 0, 0);
//     expenseDateObject.setHours(0, 0, 0, 0);

//     const differenceInMilliseconds = today - expenseDateObject;
//     const differenceInDays = differenceInMilliseconds / (1000 * 60 * 60 * 24);
     
//     if (differenceInDays === 0) {
//         return "Today";
//     }

//     if (differenceInDays === 1) {
//         return "Yesterday";
//     }

//     return `${differenceInDays} days ago`;
// }


export function handleUnauthorized() {
    localStorage.removeItem("access_token");
    window.location.href = "/";
}

export async function apiRequest(endpoint, options = {}) {
    const token = localStorage.getItem("access_token");

    const response = await fetch(endpoint, {
        ...options,
        headers: {
            "Authorization": `Bearer ${token}`,
            ...options.headers
        }
    });

    if (response.status === 401) {
        handleUnauthorized();
        return null;
    }

    const data = await response.json();

    if (!response.ok) {
        console.error("Backend error:", data);
        return {
            ok: false,
            data: data
        };
    }

    return {
        ok: true,
        data: data
    };
}