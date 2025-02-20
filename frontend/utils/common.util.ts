// import { defu } from 'defu';

// export function $http(url: string, options?: any) {
// 	const config = useRuntimeConfig();
// 	const login_token = useCookie('login_token');
// 	const settings = defu(options, {
// 		baseURL: config.public.baseURL,
// 		headers: { Authorization: `Bearer ${login_token.value ?? ''}` }
// 	});

// 	return $fetch<{ code: number; msg: string; result: any }>(url, settings);
// }

export function formatNumber(num: number, digit = 0) {
	if (num === null || num === undefined || isNaN(num)) {
		return 0;
	}
	const number = Number(num).toLocaleString('ko-KR', { maximumFractionDigits: digit });
	return number === '-0' ? '0' : number;
}

// export function stringToInt(amt: any) {
// 	if (!amt) return 0;
// 	return parseFloat(String(amt).replace(/[^0-9.-]/g, ''));
// }

// export const isEmpty = (value: any): boolean => {
// 	if (!value) return true;
// 	else if (Array.isArray(value) && value.length === 0) return true;
// 	else if (typeof value === 'object' && value !== null && Object.keys(value).length === 0) return true;

// 	return false;
// };


// export const is_empty = (value: any): boolean => {
// 	// falsy값 chk : false, 0, "", null, undefined, NaN
// 	if (!value) return true;
// 	// 빈 배열 chk
// 	if (Array.isArray(value) && value.length === 0) return true;
// 	// 빈 객체 chk
// 	if (typeof value === 'object' && value !== null && Object.keys(value).length === 0) return true;

// 	return false;
// };