import './style.css';
import './utilities.css';
import {RootProvider} from 'fumadocs-ui/provider';
export const metadata={title:{default:'Template Fieldnotes',template:'%s · Template Fieldnotes'},description:'A practical field guide to the Archont561 starter catalog.'};
export default function Layout({children}:{children:React.ReactNode}){return <html lang="en" suppressHydrationWarning><body><RootProvider search={{options:{type:'static',api:`${process.env.NEXT_PUBLIC_BASE_PATH||''}/search.json`}}}>{children}</RootProvider></body></html>}
